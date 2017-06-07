from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/', views.image_add),
    url(r'^match/', views.image_match),
]