from django.urls import path
from . import views

app_name = 'wear'

urlpatterns = [
    path('', views.product, name='product'),
    path('<slug:slug>', views.product_detail, name='product_detail')
]