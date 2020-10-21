from django.shortcuts import render
from django.db.models import Q
from rest_framework import status, permissions, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserDetailSerializer, \
	FriendSerializer, FriendRequestSerializer, BlockingFriendSerializer, \
	PartySerializer, PartyMemberSerializer
from .models import User, UserDetail, Friend, FriendRequest, BlockingFriend, \
	Party, PartyMember


class CreateUserView(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)


# class UpdateUserView(generics.RetrieveUpdateAPIView):
# 	serializer_class = UserSerializer
#
# 	def get_object(self):
# 		return self.request.user
#
#
# class DeleteUserView(generics.DestroyAPIView):
# 	serializer_class = UserSerializer
#
# 	def get_object(self):
# 		return self.request.user
#
# 	def perform_destroy(self, instance):
# 		instance.is_active = False
# 		instance.save()


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def get_queryset(self):
		return self.queryset.filter(id=self.request.user.id)

	def create(self, request, *args, **kwargs):
		response = {'message': 'CREATE method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def perform_create(self, serializer):
		response = {'message': 'CREATE method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class UserDetailViewSet(viewsets.ModelViewSet):
	serializer_class = UserDetailSerializer
	queryset = UserDetail.objects.all()

	def get_queryset(self):
		return self.queryset.filter(is_active=True)

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class FriendViewSet(viewsets.ModelViewSet):
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(Q(is_active=True) & Q(user_id=self.request.user))

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class FriendRequestViewSet(viewsets.ModelViewSet):
	serializer_class = FriendRequestSerializer
	queryset = FriendRequest.objects.all()

	def get_queryset(self):
		return self.queryset.filter(
			Q(is_active=True)
			&
			(Q(src_user_id=self.request.user) | Q(dest_user_id=self.request.user))
		)

	def perform_create(self, serializer):
		serializer.save(src_user_id=self.request.user)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class BlockingFriendViewSet(viewsets.ModelViewSet):
	serializer_class = BlockingFriendSerializer
	queryset = BlockingFriend.objects.all()

	def get_queryset(self):
		return self.queryset.filter(is_active=True)

	def perform_create(self, serializer):
		serializer.save(is_active=True)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class PartyViewSet(viewsets.ModelViewSet):
	serializer_class = PartySerializer
	queryset = Party.objects.all()

	def get_queryset(self):
		return self.queryset.filter(Q(is_active=True) & Q(user_id=self.request.user))

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user, is_active=True)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()


class PartyMemberViewSet(viewsets.ModelViewSet):
	serializer_class = PartyMemberSerializer
	queryset = PartyMember.objects.all()

	def get_queryset(self):
		return self.queryset.filter(Q(is_active=True) & Q(user_id=self.request.user) & Q(party_id__user_id=self.request.user))

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user, is_active=True)

	def perform_destroy(self, instance):
		instance.is_active = False
		instance.save()
