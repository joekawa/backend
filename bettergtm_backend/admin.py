from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(Customer)
admin.site.register(Release)
admin.site.register(ReleaseActivity)
admin.site.register(Profile)
admin.site.register(Goal)

# Register your models here.
