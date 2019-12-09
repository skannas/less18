from django.urls import path
from .views import *

urlpatterns = [
    path('', getProduct),
    path('indexmy', getIndexMy),
]
