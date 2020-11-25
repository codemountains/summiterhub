from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import PlanSerializer, PlanGearSerializer, \
	PlanCustomGearSerializer, PlanRouteSerializer, PlanRouteDetailSerializer, \
	PlanEscapeRouteSerializer, PlanMemberSerializer, BookmarkSerializer, \
	PlanSearchSerializer
from .models import Plan, PlanGear, PlanCustomGear, PlanRoute, \
	PlanRouteDetail, PlanEscapeRoute, PlanMember, Bookmark
from .filters import PlanSearchFilter
from .paginations import PlanBasePagination


class PlanViewSet(viewsets.ModelViewSet):
	"""
	登山計画 ModelViewSet
	"""
	serializer_class = PlanSerializer
	queryset = Plan.objects.all()
	filter_class = PlanSearchFilter
	pagination_class = PlanBasePagination

	def get_queryset(self):
		param_mountain = self.request.query_params.get('mountain')

		if param_mountain is None:
			return self.queryset.filter(
				created_user=self.request.user
			).order_by('-entering_date').order_by('-descending_date')

		return self.queryset.filter(
			(
					Q(mountain_first__contains=param_mountain)
					| Q(mountain_second__contains=param_mountain)
					| Q(mountain_third__contains=param_mountain)
					| Q(mountain_fourth__contains=param_mountain)
					| Q(mountain_fifth__contains=param_mountain)
			)
			&
			Q(created_user=self.request.user)
		).order_by('-entering_date').order_by('-descending_date')

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanGearViewSet(viewsets.ModelViewSet):
	"""
	登山計画装備 ModelViewSet
	"""
	serializer_class = PlanGearSerializer
	queryset = PlanGear.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(plan_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanCustomGearViewSet(viewsets.ModelViewSet):
	"""
	登山計画カスタム装備 ModelViewSet
	"""
	serializer_class = PlanCustomGearSerializer
	queryset = PlanCustomGear.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(plan_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanRouteViewSet(viewsets.ModelViewSet):
	"""
	登山計画ルート ModelViewSet
	"""
	serializer_class = PlanRouteSerializer
	queryset = PlanRoute.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(plan_id=self.kwargs.get('plan_id')).order_by('plan_date')

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanRouteDetailViewSet(viewsets.ModelViewSet):
	"""
	登山計画ルート詳細 ModelViewSet
	"""
	serializer_class = PlanRouteDetailSerializer
	queryset = PlanRouteDetail.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(
			plan_route_id=self.kwargs.get('plan_route_id')).order_by('sort_index')

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanEscapeRouteViewSet(viewsets.ModelViewSet):
	"""
	登山計画エスケープルート ModelViewSet
	"""
	serializer_class = PlanEscapeRouteSerializer
	queryset = PlanEscapeRoute.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(plan_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class PlanMemberViewSet(viewsets.ModelViewSet):
	"""
	登山計画メンバー ModelViewSet
	"""
	serializer_class = PlanMemberSerializer
	queryset = PlanMember.objects.all()
	pagination_class = None

	def get_queryset(self):
		return self.queryset.filter(plan_id=self.kwargs.get('plan_id')).order_by('sort_index')

	def perform_create(self, serializer):
		serializer.save(
			created_user=self.request.user,
			updated_user=self.request.user
		)

	def perform_update(self, serializer):
		serializer.save(updated_user=self.request.user)


class BookmarkViewSet(viewsets.ModelViewSet):
	"""
	ブックマーク ModelViewSet
	"""
	serializer_class = BookmarkSerializer
	queryset = Bookmark.objects.all()
	pagination_class = PlanBasePagination

	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(user=self.request.user)
		except BaseException:
			raise ValidationError('この計画はブックマーク済みです')

	def update(self, request, *args, **kwargs):
		response = {'message': 'PUT method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, *args, **kwargs):
		response = {'message': 'PATCH method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PlanSearchViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	登山計画検索 ReadOnlyModelViewSet
	提出済みの計画のみ抽出可能
	"""
	serializer_class = PlanSearchSerializer
	queryset = Plan.objects.all()
	permission_classes = (AllowAny,)
	filter_class = PlanSearchFilter
	pagination_class = PlanBasePagination

	def get_queryset(self):
		param_mountain = self.request.query_params.get('mountain')

		if param_mountain is None:
			return self.queryset.filter(is_submitted=True).order_by('-updated_at')

		return self.queryset.filter(
			(
					Q(mountain_first__contains=param_mountain)
					| Q(mountain_second__contains=param_mountain)
					| Q(mountain_third__contains=param_mountain)
					| Q(mountain_fourth__contains=param_mountain)
					| Q(mountain_fifth__contains=param_mountain)
			)
			&
			Q(is_submitted=True)
		).order_by('-entering_date')
