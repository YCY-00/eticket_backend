from django.contrib import admin

from backend.event.models import EventModel

@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer', 'capacity', 'remaining_capacity')
    search_fields = ('title', 'location', 'organizer__name')
    list_filter = ('date', 'organizer__name')
    ordering = ('date', 'organizer__name')
    readonly_fields = ('remaining_capacity',)
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'location', 'organizer', 'capacity', 'remaining_capacity')
        }),
    )
