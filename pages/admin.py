from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.fotografia.url))

    thumbnail.short_description = 'Fotografia'

    list_display = ('id', 'thumbnail', 'emri', 'pozita')
    

admin.site.register(Team, TeamAdmin)
