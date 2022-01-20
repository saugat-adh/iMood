from django.urls import path

from .views import medicationView, medicationDetailView

urlpatterns =[
    path('list/', medicationView.as_view()),
    path('<int:id>/', medicationDetailView.as_view()),
]