from django.urls import path
from . import views


urlpatterns = [
    path("", views.index), #when we go to the main page - we take method from views and show users html
    path("about-us", views.about),
]