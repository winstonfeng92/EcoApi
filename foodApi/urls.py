"""
URL configuration for foodApi project.

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
from django.urls import path,include
from backend.views import *  # Import the view
from backend.views import FoodItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'fooditems', FoodItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world, name='hello_world'),  # Map the view to a URL,
    path('', showItemDetails, name='hello_world'),  # Map the view to a URL,
    path('items', showItemDetails, name='show_items'),  # Map the view to a URL,
    path('items/<str:name>/', match_product, name='match_product'),
    path('api/', include(router.urls)),

]



