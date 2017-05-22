from django.contrib import admin

from .models import Rank, RankRegister, RankPreset


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'are_mentors', 'prev', )
    list_editable = ('name', 'are_mentors', 'prev', )
    list_display_links = ('id', )
    ordering = ('id', 'name', 'prev', )


@admin.register(RankRegister)
class RankRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'mentor', 'junior', 'rank', )
    list_display_links = ('id', 'mentor', 'junior', 'rank', )
    list_filter = ('mentor', 'rank', )
    search_fields = (
        'mentor__firstname', 'mentor__lastname',
        'junior__firstname', 'junior__lastname',
    )
    ordering = ('id', 'rank', 'mentor', 'junior', )


@admin.register(RankPreset)
class RankPresetAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'rank', 'limit', )
    list_editable = ('state', 'rank', 'limit', )
    list_display_links = ('id', )
