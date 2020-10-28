from django.db.models import Q
from django.utils import timezone
from django.core.mail import EmailMessage
from rest_framework import status, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserTokenSerializer, \
	UserDetailSerializer, FriendSerializer, FriendRequestSerializer, \
	BlockingFriendSerializer, PartySerializer, PartyMemberSerializer
from .models import User, UserDetail, UserToken, Friend, FriendRequest, \
	BlockingFriend, Party, PartyMember

import datetime
import hashlib


class CreateUserView(generics.CreateAPIView):
	"""
	ユーザ作成 CreateAPIView
	ユーザをis_active=Falseで作成 > UserTokenCreateViewで認証トークンを発行
	"""
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
	"""
	ユーザ情報 ModelViewSet
	"""
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def get_queryset(self):
		return self.queryset.filter(id=self.request.user.id)

	# 新規作成は不可
	def create(self, request, *args, **kwargs):
		response = {'message': 'ユーザ詳細情報の作成はできません'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	# 新規作成は不可
	def perform_create(self, serializer):
		response = {'message': 'ユーザ詳細情報の作成はできません'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserTokenCreateView(generics.CreateAPIView):
	"""
	ユーザ認証トークン CreateAPIView
	"""
	serializer_class = UserTokenSerializer
	queryset = UserToken.objects.all()
	permission_classes = (AllowAny,)

	def perform_create(self, serializer):
		param_user_id = self.request.query_params.get('user_id')
		user = User.objects.filter(id=param_user_id).first()

		if user is None:
			raise ValidationError('ユーザが見つかりません')

		if user.is_active:
			raise ValidationError('ユーザはすでに認証済みです')

		# UserToken
		if UserToken.objects.filter(user=user).exists():
			UserToken.objects.get(user=user).delete()

		# Tokenを生成
		now = timezone.now()
		non_hash_token = user.email + user.password + now.strftime('%Y%m%d%H%M%S%f')
		hashed_token = hashlib.sha1(non_hash_token.encode('utf-8')).hexdigest()
		expiration_at = now + datetime.timedelta(days=1)

		created_user_token = serializer.save(
			user=user,
			email=user.email,
			token=hashed_token,
			expiration_at=expiration_at
		)

		auth_url = 'https://sumitterhub.com/v1/uses/tokens/activate/{0}/?token={1}'.format(
			created_user_token.id,
			created_user_token.token
		)

		# メールを送信
		subject = 'SummiterHub メールアドレス確認'
		message = '{0} 様　\n新規登録ありがとうございます。\nURL: {1}'.format(user.email, auth_url)
		from_email = 'info@summiterhub.com'
		to_list = [user.email]
		cc_list = []
		bcc_list = []

		message = EmailMessage(
			subject=subject,
			body=message,
			from_email=from_email,
			to=to_list,
			cc=cc_list,
			bcc=bcc_list
		)
		message.send()


class UserTokenUpdateView(generics.UpdateAPIView):
	"""
	ユーザ認証トークン UpdateAPIView
	"""
	serializer_class = UserTokenSerializer
	queryset = UserToken.objects.all()
	permission_classes = (AllowAny,)

	def perform_update(self, serializer):
		# Tokenの確認
		user_token = UserToken.objects.filter(
			Q(id=self.kwargs.get('pk'))
			&
			Q(token=self.request.query_params.get('token'))
		).first()

		if user_token is None:
			raise ValidationError('認証に失敗しました')
		if timezone.now() > user_token.expiration_at:
			raise ValidationError('認証の有効期限(24時間)を超えています')

		user = User.objects.filter(id=user_token.user.id).first()
		if user is None:
			raise ValidationError('ユーザが存在しません')
		user.is_active = True
		user.save()


class UserDetailViewSet(viewsets.ModelViewSet):
	"""
	ユーザ詳細 ModelViewSet
	"""
	serializer_class = UserDetailSerializer
	queryset = UserDetail.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(user=self.request.user)
		except BaseException:
			raise ValidationError('すでにユーザ詳細を作成済みです')


class FriendViewSet(viewsets.ModelViewSet):
	"""
	フレンド ModelViewSet
	"""
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(
			Q(src_user=self.request.user) | Q(dest_user=self.request.user)
		)

	def perform_create(self, serializer):
		try:
			serializer.save()
		except BaseException:
			raise ValidationError('すでにフレンドです')


class FriendDetailViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	フレンド詳細 ReadOnlyModelViewSet
	"""
	serializer_class = UserDetailSerializer
	queryset = UserDetail.objects.all()

	def get_queryset(self):
		friend = Friend.objects.filter(
			Q(id=self.kwargs.get('friend_id'))
			&
			Q(src_user=self.request.user)
		).first()

		if friend is None:
			return None
		return self.queryset.filter(user=friend.dest_user)


class FriendRequestViewSet(viewsets.ModelViewSet):
	"""
	フレンド申請 ModelViewSet
	"""
	serializer_class = FriendRequestSerializer
	queryset = FriendRequest.objects.all()

	def get_queryset(self):
		return self.queryset.filter(
			Q(src_user=self.request.user)
			|
			(Q(dest_user=self.request.user) | Q(
				dest_email=self.request.user.email))
		)

	def perform_create(self, serializer):
		data_dest_email = serializer.validated_data.get('dest_email')
		user = User.objects.filter(email=data_dest_email).first()

		if user == self.request.user:
			raise ValidationError('自分にフレンド申請はできません')

		try:
			serializer.save(src_user=self.request.user, dest_user=user)
		except BaseException:
			raise ValidationError('すでにフレンド申請済みです')

	def perform_update(self, serializer):
		friend_request = self.queryset.filter(id=self.kwargs.get('pk')).first()
		dest_user = friend_request.dest_user

		if dest_user is not None:
			if dest_user != self.request.user:
				raise ValidationError('申請されたリクエストのみ承認または拒否できます')

		serializer.save()


class BlockingFriendViewSet(viewsets.ModelViewSet):
	"""
	ブロックフレンド ModelViewSet
	"""
	serializer_class = BlockingFriendSerializer
	queryset = BlockingFriend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(src_user=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(src_user=self.request.user)
		except BaseException:
			raise ValidationError('すでにブロック済みです')


class PartyViewSet(viewsets.ModelViewSet):
	"""
	パーティ ModelViewSet
	"""
	serializer_class = PartySerializer
	queryset = Party.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class PartyMemberViewSet(viewsets.ModelViewSet):
	"""
	パーティメンバー ModelViewSet
	"""
	serializer_class = PartyMemberSerializer
	queryset = PartyMember.objects.all()

	def get_queryset(self):
		return self.queryset.filter(party_id_id=self.kwargs.get('party_id'))

	def perform_create(self, serializer):
		serializer.save(
			user=self.request.user,
			party_id=self.kwargs.get('party_id')
		)


class PartyMemberDetailViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	パーティメンバー詳細 ReadOnlyModelViewSet
	"""
	serializer_class = UserDetailSerializer
	queryset = UserDetail.objects.all()

	def get_queryset(self):
		party_member = PartyMember.objects.filter(
			Q(id=self.kwargs.get('party_member_id'))
			&
			Q(party_id=self.kwargs.get('party_id'))
			&
			Q(user=self.request.user)
		).first()
		if party_member is None:
			return None

		friend = Friend.objects.filter(
			Q(src_user=self.request.user)
			&
			Q(dest_user=party_member.entry_user)
		).first()
		if friend is None:
			return None

		return self.queryset.filter(user=friend.dest_user)
