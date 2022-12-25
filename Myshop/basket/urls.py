from django.urls import path, include
from rest_framework import routers
from . import views
from . import basket
#from home.models import Product
app_name = 'basket'

# router = routers.DefaultRouter()
# router.register(r'basket', )


urlpatterns = [
    # path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('basket', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),
    path('delete/', views.basket_delete, name='basket_delete'),
    path('update/', views.basket_update, name='basket_update'),
    path('^send/', views.send_tg, name='send'),
]