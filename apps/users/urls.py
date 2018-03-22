from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.all_users),
    path('<int:id>', views.view_user),
    path('new', views.new_user),
    path('new/create', views.create_user),
    path('<int:id>/edit', views.edit_user),
    path('<int:id>/edit/update', views.update_user),
    path('<int:id>/destroy', views.destroy_user),
]