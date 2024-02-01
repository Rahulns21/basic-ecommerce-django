from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'), 
    path('item/<int:pk>/', views.detail, name='detail'),
    path('checkout/',views.checkout, name='checkout'),
]
