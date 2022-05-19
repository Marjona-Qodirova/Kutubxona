from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# admin.site.register(Muallif)
admin.site.register(Student)
admin.site.register(Record)
@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ("nom", "id", "sahifa",)
    list_editable = ("sahifa","janr",)
    list_filter = ("janr",)
    list_display = ("id","nom","sahifa","janr")



    autocomplete_fields = ("muallif",)








# @admin.register(Student)
# class StudentAdmin(ModelAdmin):
#     search_fields = ("ism", "id","guruh",)
#     list_editable = ("ism","kitob_soni",)
#     list_filter = ("guruh",)
#     list_display = ("id","ism","guruh","kitob_soni")
@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields=("ism",)
    list_display = ("id","ism","yosh","tirik")
    list_display_links = ("ism",)
    list_editable = ("yosh","tirik",)
    list_filter = ("tirik",)




