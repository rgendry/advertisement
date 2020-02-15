from django.urls import path
from ads.views import *

urlpatterns = [
    path('ad/create/', AdCreateView.as_view()),
    path('all/', AdsListView.as_view()),
    path('ad/create/<int:pk>', AdDetailView.as_view()),
]