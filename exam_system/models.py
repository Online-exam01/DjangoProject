from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    title = models.CharField(max_length=255)


description = models.TextField()
duration = models.IntegerField(help_text="Duration in minutes")
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title


class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions',
                             on_delete=models.CASCADE)


question_text = models.CharField(max_length=255)
answer_a = models.CharField(max_length=255)
answer_b = models.CharField(max_length=255)
answer_c = models.CharField(max_length=255)
answer_d = models.CharField(max_length=255)
correct_answer = models.CharField(max_length=1)  # 'A', 'B', 'C',
'D'


def __str__(self):
    return self.question_text


class StudentExam(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)


exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
score = models.FloatField(null=True, blank=True)
completed_at = models.DateTimeField(null=True, blank=True)


def __str__(self):
    return f"{self.student.username} - {self.exam.title}"


from django.db import models

#from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# class Exam(models.Model):
# title = models.CharField(max_length=255)
# description = models.TextField()
# duration = models.IntegerField(help_text="Duration in minutes")
# created_at = models.DateTimeField(auto_now_add=True)
# def __str__(self):
# return self.title
# class Question(models.Model):
# exam = models.ForeignKey(Exam, related_name='questions',
# on_delete=models.CASCADE)
# question_text = models.CharField(max_length=255)
# answer_a = models.CharField(max_length=255)
# answer_b = models.CharField(max_length=255)
# answer_c = models.CharField(max_length=255)
# answer_d = models.CharField(max_length=255)
# correct_answer = models.CharField(max_length=1) # 'A', 'B', 'C',
# 'D'
# def __str__(self):
# return self.question_text
# class StudentExam(models.Model):
# student = models.ForeignKey(User, on_delete=models.CASCADE)
# exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
# score = models.FloatField(null=True, blank=True)
# completed_at = models.DateTimeField(null=True, blank=True)
# def __str__(self):
# return f"{self.student.username} - {self.exam.title}"
# create your models here.# In views.py, implement registration and login views
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
# def register(request):
# if request.method == 'POST':
# form = UserCreationForm(request.POST)
# if form.is_valid():
# user = form.save()
# login(request, user)
# return redirect('exam_list') # Redirect to exam list page
#
# else:
# form = UserCreationForm()
# return render(request, 'register.html', {'form': form})
