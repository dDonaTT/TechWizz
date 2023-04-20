from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProduktetAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.fotografia.url))

    thumbnail.short_description = 'Fotografia'
    list_display=('id','thumbnail','lloji','emri_produktit','modeli','ngjyra','is_featured')
    list_editable = ('is_featured',)

admin.site.register(Product,ProduktetAdmin)
