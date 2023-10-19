from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentView.as_view(), name='Home'),
    path('modify/<int:pk>/', views.StudentModify.as_view(), name='Modeify'),

]