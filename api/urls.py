from django.urls import path
from api import views

urlpatterns = [
	path('converter/', views.ConverterApiView.as_view()),
]