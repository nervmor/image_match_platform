from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.phash_feature_add),
    url(r'^get/', views.phash_feature_get),
]