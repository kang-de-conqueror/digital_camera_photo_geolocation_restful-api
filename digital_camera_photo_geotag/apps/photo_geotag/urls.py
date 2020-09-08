"""digital_camera_photo_geotag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # # Get all routes
    # path("", views.get_all_routes, name='get_all_routes'),
    # Create a route
    path("create", views.create_route, name='create_route'),
    path("aws_s3/create", views.create_route_aws_s3, name='create_aws_s3'),
    # Get data of a route
    path("<str:route_UUID>", views.route_detail, name='route_detail'),
    path("aws_s3/<str:route_UUID>", views.route_detail_aws_s3, name='get_aws_s3'),
    # Delete
    path("<str:route_id>/delete/", views.delete_route, name='delete_route'),
]
