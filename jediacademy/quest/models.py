from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

from ranking.models import Rank
from reception.models import Person


class Quest(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT)
    descr = models.TextField(_("description"))

    class Meta:
        verbose_name = _("quest")
        verbose_name_plural = _("quests")
        unique_together = ('rank', 'descr', )

    def __str__(self):
        return "Level={}; {}...".format(
            self.rank.name, self.descr[:21]
        )


class Task(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.PROTECT)
    question = models.TextField(_("question"))

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
        unique_together = ('quest', 'question', )

    def __str__(self):
        return "{}; Question={}...".format(
            self.quest, self.question[:21]
        )


class Exam(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    quest = models.ForeignKey(Quest, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("exam")
        verbose_name_plural = _("exams")
        unique_together = ('person', 'quest', )

    def __str__(self):
        return "Person={}; Quest-{}".format(
            self.person, self.quest
        )

    def get_absolute_url(self):
        return reverse('exam-detail', args=[str(self.id)])


class Answer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    actual_question_text = models.TextField(_("actual question text"))
    choice = models.BooleanField(_("choice"))

    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")
        unique_together = ('exam', 'task', )

    def __str__(self):
        return "{} Task question={}...; Choice is {}".format(
            self.exam, self.task.question[:21], self.choice
        )
