from . import views
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cars/', views.car_list, name='car-list'),
    path('owners/', views.owner_list, name='owner-list'),
    path('repair/', views.repair_list, name='repair-list'),
    path('main/', views.main_page, name='main-page'),
    path('calendar/', views.calendar_page, name='calendar-page'),
    path('uslugi/', views.uslugi_page, name='uslugi-page'),
    path('contacts/', views.contact_page, name='contacts-page'),
    path('success/', views.success_page, name='success-page'),
    path('save_booking/', views.save_booking, name='save_booking-page'),
    path('bookings/', views.bookings, name='bookings-page'),
    path('lk/', views.lk_page, name='lk-page'),
    path('register/', views.register_page, name='register-page'),
    path('login/', views.login_page, name='login-page'),
    path('profile/', views.profile, name='profile-page'),
]
