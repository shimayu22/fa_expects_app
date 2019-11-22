from django.contrib import admin
from .models import Players, FaExpects, RequestedConditions

# Register your models here.
admin.site.site_header = 'FA予想管理'

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'position' , 'dominant_hand', \
                    'department',)

class FaExpectsAdmin(admin.ModelAdmin):
    list_display = ('team', 'priority', 'player_id',)

class RequestedConditionsAdmin(admin.ModelAdmin):
    list_display = ('age', 'position' , 'dominant_hand')

admin.site.register(Players, PlayersAdmin)
admin.site.register(FaExpects, FaExpectsAdmin)
admin.site.register(RequestedConditions, RequestedConditionsAdmin)