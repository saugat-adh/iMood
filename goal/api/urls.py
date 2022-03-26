from django.urls import path, include
from goal.views import GoalAV

urlpatterns = [
    path('list/', GoalAV.as_view()),
    path('goal/', GoalAV.as_view(), name='goal'),
]