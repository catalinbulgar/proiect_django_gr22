from django.urls import path
from locations import views

app_name = 'locations'

urlpatterns = [
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
]
