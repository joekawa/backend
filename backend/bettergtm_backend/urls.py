from django.urls import path

from . import views

app_name = "bettergtm_backend"

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("team/", views.team, name="team"),
    path("release/", views.release, name="release"),
    path("release_activity/", views.release_activity, name="release_activity"),
    path("profile/", views.profile, name="profile"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('deactivate_user/', views.deactivate_user, name='deactivate_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('update_user', views.update_user, name='update_user'),
]