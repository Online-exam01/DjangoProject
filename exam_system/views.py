from django.shortcuts import render

# Create from django.contrib.auth.decorators import login_required
# from .models import Exam, Question
# from django.shortcuts import get_object_or_404
# @login_required
# def create_exam(request):
# if request.method == 'POST':
# title = request.POST['title']
# description = request.POST['description']
# duration = request.POST['duration']
# exam = Exam.objects.create(
# title=title,
# description=description,
# duration=duration,
# )
# return redirect('exam_list') # Redirect to exam list page
# return render(request, 'create_exam.html')
#
# @login_required
# def add_question(request, exam_id):
# exam = get_object_or_404(Exam, id=exam_id)
# if request.method == 'POST':
# question_text = request.POST['question_text']
# answer_a = request.POST['answer_a']
# answer_b = request.POST['answer_b']
# answer_c = request.POST['answer_c']
# answer_d = request.POST['answer_d']
# correct_answer = request.POST['correct_answer']
# Question.objects.create(
# exam=exam,
# question_text=question_text,
# answer_a=answer_a,
# answer_b=answer_b,
# answer_c=answer_c,
# answer_d=answer_d,
# correct_answer=correct_answer,
# )
# return redirect('exam_detail', exam_id=exam.id) # Redirect to
#
# exam detail page
# return render(request, 'add_question.html', {'exam': exam})
# our views here.
