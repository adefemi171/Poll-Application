from django.urls import path

from . import views

# The path() function takes in four arguments two are required: route and view and two are optional: kwargs and name.
# route is a string that contains a URL patterm
# for view when Django finds a matching patter, it calls the specified view function with an HttpRequest object as the first argument
# view example here is "views.index"
# kwargs is an arbitrary keyword arguments and can be passed in a dictionary to the target view
# name which allows naming your url which lets you refer to it unambigously from elsewhere in DjangoTemplates
# name example here is: "name='index'"

# added an app_name so Django can differentiates the URL names between several Django projects
app_name = 'polls'
urlpatterns = [
    # /polls/
    # path("", views.index, name='index'),
    # /polls/<num>
    # removed the word specifics
    # path('<str:question_id>/', views.detail, name='detail'),
    # /polls/<num>/results
    # path('<str:question_id>/results/', views.results, name='results'),
    # /polls/<num>/vote
    # path('<str:question_id>/vote/', views.vote, name='vote'),
    # refactoring the URLconf to use generic views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk/results/>', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]