from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect

from .forms import AnswerInlineModelFormSet
from .models import Exam


class ExamCreateView(CreateView):
    model = Exam
    fields = ('person', 'quest', )


class ExamDetailView(DetailView):
    model = Exam


def create_answers_view(request, exam_id, *args, **kwargs):
    exam = Exam.objects.get(id=exam_id)
    if request.method == "POST":
        formset = AnswerInlineModelFormSet(request.POST, instance=exam)
        if formset.is_valid():
            formset.save()
            return redirect('afterparty')
    if request.method == "GET":
        tasks = exam.quest.task_set.all()
        initial = [{'exam': exam_id, 'task': t.id, 'actual_question_text': t.question} for t in tasks]
        formset = AnswerInlineModelFormSet(instance=exam, initial=initial)
    return render(request, 'quest/answers_create.html', {'formset': formset})
