from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('', views.task_list, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('tasks/create/', views.task_create, name='task_create'), # Добавьте это!
    path('tasks/<int:pk>/', views.task_delete, name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
]