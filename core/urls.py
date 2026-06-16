from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Админка
    path('admin/', admin.site.urls),

    # 2. Логин, логаут и управление сессиями (встроенные механизмы Django)
    path('accounts/', include('django.contrib.auth.urls')),

    # 3. Маршруты приложения пользователей (список, редактирование, регистрация)
    path('accounts/', include('users.urls')),

    # 4. Главная страница и управление задачами
    path('', include('tasks.urls')),
]