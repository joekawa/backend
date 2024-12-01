from django.urls import path

from . import views

app_name = "bettergtm_backend"

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("team/", views.team, name="team"),
    path("release/", views.release, name="release"),
    path("release_activity/", views.release_activity, name="release_activity"),
    path("profile/", views.profilt, name="profile"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
]