from django.views.generic import ListView, CreateView
from django.db.models import Q, Count

from reception.models import Person
from .models import RankRegister


class MentorList(ListView):
    ordering = ('-juniors_count', 'lastname', 'firstname')
    template_name = 'ranking/mentor_list.html'

    def get_queryset(self):
        self.queryset = Person.objects.exclude(
            Q(juniors__rank__are_mentors=False),
        ).annotate(
            juniors_count=Count('mentors')
        ).filter(
            juniors_count__gte=self.kwargs["threshold"]
        )
        return super().get_queryset()


class RankRegisterCreate(CreateView):
    model = RankRegister
    fields = ('mentor', 'rank', 'junior', )