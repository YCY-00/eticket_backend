from django.contrib import admin

from backend.ticket.models import TicketModel

@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'price', 'updated_at', 'created_at')
    list_filter = ('event', 'price', 'updated_at', 'created_at')
    search_fields = ('event', 'price', 'updated_at', 'created_at')
