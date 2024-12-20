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
    path('activity_detail/<activity_id>',  views.activity_detail  , name='activity_detail'),
    path('release_detail/<release_id>',  views.release_detail  , name='release_detail'),
    path('goal_detail/<goal_id>',  views.goal_detail  , name='goal_detail'),
    path('update_customer/<customer_id>',  views.update_customer  , name='update_customer'),
    path('update_team/<team_id>',  views.update_team  , name='update_team'),
    path('update_release/<release_id>',  views.update_release  , name='update_release'),
    path('update_activity/<activity_id>',  views.update_activity  , name='update_activity'),
    path('update_goal/<goal_id>',  views.update_goal  , name='update_goal'),
    path('create_activity',  views.create_activity  , name='create_activity'),
    path('create_release',  views.create_release  , name='create_release'),
    path('create_role',  views.create_role, name='create_role'),
    path('create_goal',  views.create_goal, name='create_goal'),
    path('release_list',  views.release_list_view, name='release_list'),
    path('activity_list',  views.activity_list_view, name='activity_list'),
    path('goal_list',  views.goal_list_view, name='goal_list'),
    path('admin_view',  views.admin_view, name='admin_view'),
]