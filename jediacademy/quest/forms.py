from django.forms import inlineformset_factory, HiddenInput, Textarea

from .models import Exam, Answer


AnswerInlineModelFormSet = inlineformset_factory(
    Exam,
    Answer,
    fields=('exam', 'task', 'actual_question_text', 'choice', ),
    widgets={'exam': HiddenInput(), 'task': HiddenInput(),
             'actual_question_text': Textarea(attrs={'readonly': 'readonly'})},
    can_delete=False,
)
