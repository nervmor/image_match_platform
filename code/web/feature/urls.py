from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^phash/add/', views.phash_feature_add),
    url(r'^phash/get/', views.phash_feature_get),
]