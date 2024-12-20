"""THIS HELPER FILE IS FOR CUSTOM FUNCTIONS THAT SIMPLIFY DEVELOPMENT
  THINGS LIKE DELETING DATABASE OBJECTS OR UPDATING DATABASE OBJECTS"""

from apps import BettergtmBackendConfig as apps
from django.contrib.auth.models import User

def delete_all_data():
  for model in apps.get_models():
    if model != User:
      model.objects.all().delete()