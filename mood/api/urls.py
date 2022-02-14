from django.urls import path

from .views import MoodView, MoodDetailView, reasonsTagsView, reasonsTagsDetailView, feelingsTagsView, feelingsTagsDetailView, imageModelView

urlpatterns = [
    #for mood model
    path('list/', MoodView.as_view()),
    path('<int:id>/', MoodDetailView.as_view()),
    
    #for feelings tags model
    path('feelings/', feelingsTagsView.as_view()),
    path('feelings/<int:id>/', feelingsTagsDetailView.as_view()),
    
    #for reasons tags model
    path('reasons/', reasonsTagsView.as_view()),
    path('reason/<int:id>/', reasonsTagsDetailView.as_view()),
    
    #images model
    path('images/', imageModelView.as_view()),
]