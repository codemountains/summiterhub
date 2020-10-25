from django_filters import rest_framework as filters
from .models import Plan


class PlanSearchFilter(filters.FilterSet):
	"""
	登山計画検索フィルタ
	"""
	purpose_type = filters.ChoiceFilter(
		choices=Plan.PURPOSE_TYPE,
		lookup_expr='exact'
	)
	mountain_first = filters.CharFilter(lookup_expr='contains')
	mountain_second = filters.CharFilter(lookup_expr='contains')
	mountain_third = filters.CharFilter(lookup_expr='contains')
	mountain_fourth = filters.CharFilter(lookup_expr='contains')
	mountain_fifth = filters.CharFilter(lookup_expr='contains')
	from_entering_date = filters.DateFilter(
		field_name='entering_date',
		lookup_expr='gte'
	)
	to_entering_date = filters.DateFilter(
		field_name='entering_date',
		lookup_expr='lte'
	)

	class Meta:
		model = Plan
		fields = [
			'purpose_type',
			'mountain_first',
			'mountain_second',
			'mountain_third',
			'mountain_fourth',
			'mountain_fifth',
			'from_entering_date',
			'to_entering_date'
		]
