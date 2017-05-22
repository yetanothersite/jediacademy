from django.contrib import admin

from quest.models import Exam
from .models import Planet, Person


class ExamInline(admin.TabularInline):
    model = Exam
    readonly_fields = ('quest', )
    show_change_link = True
    can_delete = False
    extra = 0
    max_num = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'email', 'planet', )
    list_display_links = ('id', )
    list_editable = ('lastname', 'firstname', 'email', 'planet', )
    search_fields = ('lastname', 'firstname', 'email', )
    list_filter = ('planet', )
    ordering = ('id', 'lastname', 'firstname', 'planet', )
    inlines = (ExamInline, )


class PersonInline(admin.TabularInline):
    model = Person
    readonly_fields = ('lastname', 'firstname', 'email', )
    show_change_link = True
    can_delete = False
    extra = 0
    max_num = 0


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    ordering = ('id', 'name', )
    inlines = (PersonInline, )
