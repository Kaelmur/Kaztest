from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


def home(request):
    return render(request, "app/index.html")


class QuestionListView(ListView):
    model = models.CourseQuestion
    template_name = 'app/questions.html'
    context_object_name = 'questions'


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = models.CourseQuestion
    fields = ["question_text", "answers1", "answers2", "answers3", "answers4", "answers5", "answers6", "correct_answer", "category"]
    success_url = "/"

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if self.test_func():
            form.instance.user = self.request.user
            messages.success(self.request, 'Question created successfully!')
            return super().form_valid(form)


# @login_required
# def add_to_course(request, question_id)


