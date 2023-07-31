"""
URL configuration for LunchVote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import UserViewSet, RestaurantViewSet, VoteViewSet, SlotViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('places', RestaurantViewSet, basename='place')
router.register('votes', VoteViewSet, basename='vote')
router.register('slots', SlotViewSet, basename='slot')

urlpatterns = router.urls

urlpatterns += [
    path('', include("mainapp.urls")),
    path('admin/', admin.site.urls),
]