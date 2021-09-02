from django.urls import path

from .import views

urlpatterns = [
    path('',views.index ,name = "index"),
    # ex: /app/5/
    path('choices', views.votes , name='choices'),
    # ex: /app/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]