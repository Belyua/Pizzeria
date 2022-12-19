from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'basket'

router = routers.DefaultRouter()
router.register(r'basket', views.BasketViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('basket', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),
    path('delete/', views.basket_delete, name='basket_delete'),
    path('update/', views.basket_update, name='basket_update'),
]