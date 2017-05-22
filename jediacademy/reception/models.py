from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _


class Planet(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("planet")
        verbose_name_plural = _("planets")

    def __str__(self):
        return self.name


class Person(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.PROTECT)
    lastname = models.CharField(_("lastname"), max_length=50)
    firstname = models.CharField(_("firstname"), max_length=50)
    email = models.EmailField(_("email"), unique=True)

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return "{} {}; From={}".format(
            self.lastname, self.firstname, self.planet)

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])
