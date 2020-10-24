from django.contrib import admin
from .models import Plan, PlanGear, PlanCustomGear, PlanRoute, \
	PlanRouteDetail, PlanEscapeRoute, PlanMember, Bookmark

admin.site.register(Plan)
admin.site.register(PlanGear)
admin.site.register(PlanCustomGear)
admin.site.register(PlanRoute)
admin.site.register(PlanRouteDetail)
admin.site.register(PlanEscapeRoute)
admin.site.register(PlanMember)
admin.site.register(Bookmark)
