from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import MoodView, MoodDetailView, reasonsTagsView, reasonsTagsDetailView, feelingsTagsView, feelingsTagsDetailView, imageModelView, deleteImage

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
    path('images/delete/', deleteImage.as_view())
]