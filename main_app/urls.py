from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='detail'),
    path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
]
