from django.urls import path,include
from . import views

urlpatterns = [
    path('all', views.GetProducts.as_view()),
    path('<slug>', views.GetProduct.as_view()),
    path('types', views.GetTypes.as_view()),
]
