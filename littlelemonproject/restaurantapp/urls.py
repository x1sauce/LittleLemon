from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    # path('bookings/', views.bookingview.as_view(), name='bookings'),
    path('users/', views.UserViewSet.as_view({'get': 'list'})),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu-items/', views.MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
