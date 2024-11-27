from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(Role)
admin.site.register(Customer)
admin.site.register(Release)
admin.site.register(ReleaseActivity)
admin.site.register(Profile)

# Register your models here.
