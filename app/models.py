from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class CourseQuestion(models.Model):
    question_text = models.CharField(max_length=100)
    answers1 = models.CharField(max_length=100)
    answers2 = models.CharField(max_length=100)
    answers3 = models.CharField(max_length=100)
    answers4 = models.CharField(max_length=100)
    answers5 = models.CharField(max_length=100)
    answers6 = models.CharField(max_length=100)
    correct_answer = models.CharField(choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"), ("F", "F")], max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=[('Dialog', 'Dialog'), ('Grammar', 'Grammar'), ('Reading', 'Reading')], max_length=100)


class Dialog(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_test = models.FileField("Select audiofile",
                                  validators=[FileExtensionValidator(allowed_extensions=["mp3", "mp4"])],
                                  upload_to="media/")
    questions = models.ForeignKey(CourseQuestion, on_delete=models.CASCADE)


class Grammar(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(CourseQuestion, on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    dialogs = models.ForeignKey(Dialog, on_delete=models.CASCADE)
