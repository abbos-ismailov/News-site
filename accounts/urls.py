from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth.views import (LoginView, 
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView
                                       )
from .views import RegistrationView, MyProfileView, MyProfileUpdateView


urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', LogoutView.as_view(), name="profile"),
    path('password_change/', PasswordChangeView.as_view(), name="password_change"), ### Password changing started
    path('password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"), ### Template 

    path('password_reset/', PasswordResetView.as_view(), name="password_reset"), ### When Password is forgotten
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/complate/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('my-profile/', MyProfileView.as_view(), name="my_profile"),
    path('my-profile-update/<int:pk>', MyProfileUpdateView.as_view(), name="my_profile_update"),
]