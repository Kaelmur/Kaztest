from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ["question_text", "answers1", "answers2", "answers3", "answers4", "answers5", "answers6",
                  "correct_answer"]
