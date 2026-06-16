from django.urls import path
from . import views  # Импортируем views именно из папки users!

urlpatterns = [
    path('', views.user_list, name='user_list'),

    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
]
