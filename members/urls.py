from django.urls import path
from .views import (UserRegisterView, 
                    DashboardView, 
                    UserEditView
                    )


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('dashoard/', DashboardView.as_view(), name='dashboard'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
