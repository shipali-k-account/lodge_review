from django.urls import path  
from . import views
from django.contrib.auth import views as auth_views
from reviews.views import run_setup

urlpatterns = [
    path('review/', views.submit_review, name='submit_review'),

    
    path('login/', auth_views.LoginView.as_view(template_name='reviews/login.html'), name='login'),

   
    path('dashboard/', views.admin_dashboard, name='dashboard'),

  
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('run-setup/', run_setup, name='run_setup'),


]
