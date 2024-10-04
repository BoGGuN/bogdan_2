from django.urls import path
from bogdan_2_app.views import index

urlpatterns = [
    path('', index),
]