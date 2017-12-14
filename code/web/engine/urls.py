from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^phash_match/', views.phash_match),
]