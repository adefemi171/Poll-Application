from django.urls import path

from . import views

# The path() function takes in four arguments two are required: route and view and two are optional: kwargs and name.
# route is a string that contains a URL patterm
# for view when Django finds a matching patter, it calls the specified view function with an HttpRequest object as the first argument
# view example here is "views.index"
# kwargs is an arbitrary keyword arguments and can be passed in a dictionary to the target view
# name which allows naming your url which lets you refer to it unambigously from elsewhere in DjangoTemplates
# name example here is: "name='index'"
urlpatterns = [
    path("", views.index, name='index'),
]