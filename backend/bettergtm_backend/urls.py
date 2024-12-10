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
    path('update_user', views.update_user, name='upd    ate_user'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('customer_list',  views.customer_list_view, name='customer_list'),
    path('create_team',  views.create_team, name='create_team'),
    path('teams',  views.teams, name='teams'),
    path('customer_detail/<customer_id>',  views.customer_detail  , name='customer_detail'),
    path('team_detail/<team_id>',  views.team_detail  , name='team_detail'),
    path('update_customer/<customer_id>',  views.update_customer  , name='update_customer'),
    path('update_team/<team_id>',  views.update_team  , name='update_team'),
]