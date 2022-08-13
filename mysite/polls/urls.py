from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.PollsListView.as_view(),
         name='polls_list'),
    path('<int:pk>/', views.PollDetailView.as_view(),
         name='poll_detail'),
    path('<int:pk>/results/', views.PollResultsView.as_view(),
         name='poll_results'),
    path('<int:question_id>/vote/', views.vote,
         name='poll_vote'),
]
