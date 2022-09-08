from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('message', views.message, name='message')
]
