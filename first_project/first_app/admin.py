from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, User, UserProfileInfo
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
admin.site.register(UserProfileInfo)
