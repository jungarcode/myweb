
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='index'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('portfolio/',portfolio,name='portfolio'),
    path('<slug:slug>/',detailPost,name='detail_post'),
]
