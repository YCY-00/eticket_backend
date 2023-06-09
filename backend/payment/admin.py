from django.contrib import admin

from backend.payment.models import PaymentModel

# Register your models here.

@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'customer', 'is_refunded')
    list_filter = ('is_refunded',)
    search_fields = ('id', 'ticket__event__title', 'customer__name')
    ordering = ('-created_at',)
