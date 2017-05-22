from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ExamCreateView, ExamDetailView, create_answers_view


urlpatterns = [
    url(r'exam/person/(?P<applicant_id>\d+)/create/$',
        ExamCreateView.as_view(), name='exam-create'),
    url(r'exam/(?P<pk>\d+)/detail/$',
        ExamDetailView.as_view(), name='exam-detail'),
    url(r'exam/(?P<exam_id>\d+)/process/$',
        create_answers_view, name='answers-create'),
    url(
        r'exam/afterparty/$',
        TemplateView.as_view(template_name='quest/afterparty.html'),
        name='afterparty'
    ),
]
