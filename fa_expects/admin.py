from django.contrib import admin
from .models import Players, FaExpects

# Register your models here.
admin.site.site_header = 'FA予想管理'

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'position' , 'dominant_hand', \
                    'department',)

class FaExpectsAdmin(admin.ModelAdmin):
    list_display = ('priority', 'player_id',)

admin.site.register(Players, PlayersAdmin)
admin.site.register(FaExpects, FaExpectsAdmin)