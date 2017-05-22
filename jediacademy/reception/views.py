from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Person


class MainPageView(TemplateView):
    template_name = 'reception/main_page.html'


class PersonCreateView(CreateView):
    model = Person
    fields = ('lastname', 'firstname', 'planet', 'email', )

    def get_success_url(self):
        return reverse_lazy('exam-create',
                            kwargs={'applicant_id': self.object.id})


class PersonDetailView(DetailView):
    model = Person
