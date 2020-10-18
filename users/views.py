from django.shortcuts import render
from django.db.models import Q
from rest_framework import status, permissions, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserDetailSerializer
from .models import User, UserDetail


class CreateUserView(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)


class UpdateUserView(generics.RetrieveUpdateAPIView):
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user


class DeleteUserView(generics.DestroyAPIView):
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user

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
