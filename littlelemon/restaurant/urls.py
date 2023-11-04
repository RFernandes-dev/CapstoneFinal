#define URL route for index() view
from django.urls import path, include
from . import views, views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('bookings', views.bookings, name='bookings'), 
    # Django DRF View : 
    path('DRFmenu/', views.MenuItemView.as_view()),
    path('DRFmenu/<int:pk>', views.SingleMenuItemView.as_view()),
    # Obtain Token View
    path('api-token-auth/', obtain_auth_token),
    # Test View 
    path('test/', views.MenuItemView.as_view(), name='test-menu-item-view'), 
]