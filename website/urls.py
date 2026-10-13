
from django.urls import path
from website.views import *

urlpatterns = [
    path('index' , home_view),
]