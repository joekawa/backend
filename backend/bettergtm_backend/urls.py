from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("team/", views.team, name="team"),
    path("release/", views.release, name="release"),
    path("release_activity/", views.release_activity, name="release_activity"),
    path("profile/", views.profilt, name="profile"),
]