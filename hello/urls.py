from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [path("hello/<name>", views.hello_there, name="hello_there"),path("", views.home, name=""), ]
urlpatterns += staticfiles_urlpatterns()
