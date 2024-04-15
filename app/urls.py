from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="t-home"),
    path("course/new/", views.QuestionCreateView.as_view(), name="question_create"),
    path("questions/", views.QuestionListView.as_view(), name="questions")

]
