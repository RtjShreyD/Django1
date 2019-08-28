from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [path("hello/<name>", views.hello_there, name="hello_there"),
               path("home/", views.home, name="home"),
               path("about/", views.about, name="about"),
               path("contact/", views.contact, name="contact"),
                ]
urlpatterns += staticfiles_urlpatterns()
