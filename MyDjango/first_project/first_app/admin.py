from django.contrib import admin
from first_app.models import Topic, Webpage, Accessrecord
from first_app.models import UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Accessrecord)
admin.site.register(UserProfileInfo)
