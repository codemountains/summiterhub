from django.db.models import Q
from rest_framework import status, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserDetailSerializer, \
	FriendSerializer, FriendRequestSerializer, BlockingFriendSerializer, \
	PartySerializer, PartyMemberSerializer
from .models import User, UserDetail, Friend, FriendRequest, BlockingFriend, \
	Party, PartyMember


class CreateUserView(generics.CreateAPIView):
	"""
	ユーザ作成 CreateAPIView
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


class UserDetailViewSet(viewsets.ModelViewSet):
	"""
	ユーザ詳細 ModelViewSet
	"""
	serializer_class = UserDetailSerializer
	queryset = UserDetail.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user_id=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(user_id=self.request.user)
		except BaseException:
			raise ValidationError('You\'ve already created your detail.')


class FriendViewSet(viewsets.ModelViewSet):
	"""
	フレンド ModelViewSet
	"""
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(
			Q(src_user_id=self.request.user)
			&
			Q(dest_user_id=self.request.user)
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
			Q(src_user_id=self.request.user)
		).first()

		if friend is None:
			return None
		return self.queryset.filter(user_id=friend.dest_user_id)


class FriendRequestViewSet(viewsets.ModelViewSet):
	"""
	フレンド申請 ModelViewSet
	"""
	serializer_class = FriendRequestSerializer
	queryset = FriendRequest.objects.all()

	def get_queryset(self):
		return self.queryset.filter(
			(Q(src_user_id=self.request.user) | Q(dest_user_id=self.request.user))
		)

	def perform_create(self, serializer):
		try:
			data_dest_email = serializer.validated_data.get('dest_email')
			user = User.objects.filter(email=data_dest_email).first()
			serializer.save(src_user_id=self.request.user, dest_user_id=user)
		except BaseException:
			raise ValidationError('すでにフレンド申請済みです')

	def perform_update(self, serializer):
		friend_request = self.queryset.filter(id=self.kwargs.get('pk')).first()
		if friend_request.dest_user_id != self.request.user:
			raise ValidationError('申請されたリクエストのみ承認または拒否できます')
		serializer.save()


class BlockingFriendViewSet(viewsets.ModelViewSet):
	"""
	ブロックフレンド ModelViewSet
	"""
	serializer_class = BlockingFriendSerializer
	queryset = BlockingFriend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(src_user_id=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(src_user_id=self.request.user)
		except BaseException:
			raise ValidationError('You are already blocking the user.')


class PartyViewSet(viewsets.ModelViewSet):
	"""
	パーティ ModelViewSet
	"""
	serializer_class = PartySerializer
	queryset = Party.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user_id=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user)


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
			user_id=self.request.user,
			party_id_id=self.kwargs.get('party_id')
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
			Q(party_id_id=self.kwargs.get('party_id'))
			&
			Q(user_id=self.request.user)
		).first()
		if party_member is None:
			return None

		friend = Friend.objects.filter(
			Q(src_user_id=self.request.user)
			&
			Q(dest_user_id=party_member.entry_user_id)
		).first()
		if friend is None:
			return None

		return self.queryset.filter(user_id=friend.dest_user_id)
