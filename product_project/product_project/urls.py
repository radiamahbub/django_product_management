"""
URL configuration for product_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from products.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 

    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('update_product/<str:p_id>/', update_product, name = "update_product"),
    path('delete_product/<str:p_id>/', delete_product, name = "delete_product"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
