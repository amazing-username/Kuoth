from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
