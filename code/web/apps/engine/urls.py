from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^phash/match/', views.phash_match),
    url(r'^template/match/', views.template_match),
]