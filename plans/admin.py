from django.contrib import admin
from .models import Plan, PlanCustomGear, PlanMountain, PlanRoute, \
	PlanRouteDetail, PlanEscapeRoute, PlanMember, Bookmark

admin.site.register(Plan)
admin.site.register(PlanCustomGear)
admin.site.register(PlanRoute)
admin.site.register(PlanRouteDetail)
admin.site.register(PlanEscapeRoute)
admin.site.register(PlanMountain)
admin.site.register(PlanMember)
admin.site.register(Bookmark)
