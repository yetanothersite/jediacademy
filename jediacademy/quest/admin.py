from django.contrib import admin

from .models import Quest, Task, Exam, Answer


class TaskInline(admin.TabularInline):
    model = Task
    show_change_link = True
    extra = 1


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank', 'descr', )
    list_display_links = ('id', 'rank', 'descr', )
    search_fields = ('descr', )
    list_filter = ('rank', )
    ordering = ('id', 'rank', 'descr', )
    inlines = (TaskInline, )


class AnswerInline(admin.TabularInline):
    model = Answer
    can_delete = False
    show_change_link = True
    extra = 0
    max_num = 0


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'quest', )
    list_display_links = ('id', 'person', 'quest', )
    search_fields = ('person', 'quest', )
    list_filter = ('person', 'quest', )
    ordering = ('id', 'person', 'quest', )
    inlines = (AnswerInline, )
