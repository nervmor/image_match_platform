from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.image_add),
    url(r'^remove/', views.image_remove),
    url(r'^match/', views.image_match),
    url(r'^search/', views.image_search),
]