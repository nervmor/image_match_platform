from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^phash/add/', views.phash_feature_add),
    url(r'^phash/get/', views.phash_feature_get),
    url(r'^template/add/', views.template_feature_add),
    url(r'^template/get/', views.template_feature_get),
]