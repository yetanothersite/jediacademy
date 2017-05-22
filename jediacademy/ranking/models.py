from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from reception.models import Person


class Rank(models.Model):
    name = models.CharField(_("name"), max_length=12, unique=True)
    are_mentors = models.BooleanField(_("are mentors?"))
    prev = models.OneToOneField(
        'Rank', null=True, blank=True, on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("rank")
        verbose_name_plural = _("ranks")

    def __str__(self):
        return "{}; Are Mentors={} Prev={}".format(
            self.name,
            self.are_mentors,
            self.prev.name if self.prev else _("NA")
        )


class RankRegister(models.Model):
    mentor = models.ForeignKey(
        Person,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='mentors'
    )
    junior = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        related_name='juniors'
    )
    rank = models.ForeignKey(
        Rank, verbose_name=_("assigned rank"), on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("rank register")
        verbose_name_plural = _("rank registers")
        unique_together = ('junior', 'rank', )

    def __str__(self):
        return "Rank={}; Junior={}; Mentor={}".format(
            self.rank, self.junior, self.mentor or "Primary"
        )

    def clean(self):
        lim = RankPreset.objects.get(rank=self.rank).limit
        cnt = self.mentor.mentors.filter(rank=self.rank).count()
        if cnt >= lim:
            msg = 'Your recruiting limit for Rank: "{}" is over!'.format(
                self.rank.name)
            raise ValidationError(_(msg))


class RankPreset(models.Model):
    RANK_STATE_CHOICES = (
        ("ap", _("applicant")),
        ("jr", _("junior")),
    )
    state = models.CharField(_("state"), max_length=2, unique=True,
                             choices=RANK_STATE_CHOICES)
    rank = models.OneToOneField(Rank, on_delete=models.PROTECT)
    limit = models.SmallIntegerField(_("limit"))

    class Mets:
        verbose_name = _("rank preset")
        verbose_name_plural = _("rank presets")

    def __str__(self):
        return "Rank={}; State={}".format(
            self.rank, self.get_state_display()
        )
