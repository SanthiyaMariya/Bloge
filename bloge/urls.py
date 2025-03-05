
from django.urls import path
from .import views
app_name="bloge"


urlpatterns=[

path("",views.index,name="index"),
path("post/<str:post_id>/",views.detail,name="detail"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact")


]  