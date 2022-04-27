from django.contrib import admin

from .models import Trains, Line, Station

admin.site.register(Trains)
admin.site.register(Line)
admin.site.register(Station)