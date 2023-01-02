from django.contrib import admin
from .models import *


class AvtiAdmin(admin.ModelAdmin):
    list_display = ('ime', 'registracija', 'km', 'cena', 'scrapeTime')


admin.site.register(Avti, AvtiAdmin)


class FiltersAdmin(admin.ModelAdmin):
    list_display = ('userID', 'znamka', 'model', 'cena_od', 'cena_do', 'letnik_od', 'letnik_do')


admin.site.register(Filters, FiltersAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('ime', 'opis', 'veljavnost', 'userID')


admin.site.register(Users, UsersAdmin)


class RegkodeAdmin(admin.ModelAdmin):
    list_display = ('koda', 'opis')


admin.site.register(Regkode, RegkodeAdmin)




