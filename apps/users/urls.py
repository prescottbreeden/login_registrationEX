from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.all_users, name = 'users'),
    path('<int:id>', views.view_user, name = 'view_user'),
    path('new', views.new_user, name = 'new_user'),
    path('new/create', views.create_user, name = 'create_user'),
    path('<int:id>/edit', views.edit_user, name = 'edit_user'),
    path('<int:id>/update', views.update_user, name = 'update_user'),
    path('<int:id>/delete', views.delete_user, name = 'delete_user'),
]