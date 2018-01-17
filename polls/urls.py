from django.urls import path
from . import views

# In a real project, there might be multiple apps.
# When using {% url %} to generate an URL, we need a way
# to distinguish URL names between app.
# We can define a variable called app_name as following
#
# Whe using url helper function, we've to define {% url <app_name>:<url_name> %}
app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


# Use generic views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # URL patter for these two url changed from question_id to pk
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote')
]
