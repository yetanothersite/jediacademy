from django.db.models.signals import post_save
from django.dispatch import receiver

from channels import Channel

from quest.models import Exam
from ranking.models import RankPreset
from .models import RankRegister


@receiver(post_save, sender=Exam)
def exam_post_save_handler(sender, instance, created, **kwargs):
    """ New Exam's Persons has applicant's Rank """
    if created:
        applicant_rank = RankPreset.objects.get(state='ap').rank
        RankRegister.objects.create(
            mentor=None,
            rank=applicant_rank,
            junior=instance.person
        )


@receiver(post_save, sender=RankRegister)
def rank_register_post_save_handler(sender, instance, created, **kwargs):
    if instance.rank.are_mentors:
        # Mentors do not need to send
        return
    if created:
        data = {
            'rank_name': instance.rank.name,
            'email': instance.junior.email
        }
        Channel('send_rank_register_notification').send(data)
