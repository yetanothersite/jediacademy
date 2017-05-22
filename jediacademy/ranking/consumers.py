from django.core.mail import EmailMessage
from django.utils.translation import ugettext as _


def send_rank_register_notification(data):
    subject = _("Hello from JediAcademy")
    body = _("Your Rank was changed to %(rank)s") % {'rank': data['rank_name']}
    email = EmailMessage(subject, body, to=(data['email'], ))
    email.send()
