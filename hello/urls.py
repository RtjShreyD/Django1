'''This file contains the url extension paths eg. www.xyz.com/hello/home or hello/contact'''

from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [path("hello/<name>", views.hello_there, name="hello_there"),
               path("home/", views.home, name="home"),
               path("about/", views.about, name="about"),
               path("contact/", views.contact, name="contact"),
               path("log/", views.log_message, name="log"),
                ]
urlpatterns += staticfiles_urlpatterns()
