from django.urls import path
from .views import (UserRegisterView,
                    DashboardView,
                    UserEditView,
                    PasswordsChangeView,
                    UserDeleteView
                    )


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('dashoard/', DashboardView.as_view(), name='dashboard'),
    path('<int:pk>/edit_profile/',
         UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_profile'),
]
