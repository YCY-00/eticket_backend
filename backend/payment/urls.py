from django.urls import path
from .views import (
    GetPaymentTicketView,
    GetPaymentView,
    RegisterPaymentView,
    UpdatePaymentView,
    DeletePaymentView,
    GetEventPaymentsView,
    GetUserPaymentsView,
)

app_name = "payment"
urlpatterns = [
    path("payment/ticket/<str:payment_id>/", GetPaymentTicketView.as_view()),
    path("payment/<str:payment_id>/", GetPaymentView.as_view()),
    path("payment/register/", RegisterPaymentView.as_view()),
    path("payment/update/<str:payment_id>/", UpdatePaymentView.as_view()),
    path("payment/delete/<str:payment_id>/", DeletePaymentView.as_view()),
    path("event/payments/<str:event_id>/", GetEventPaymentsView.as_view()),
    path("user/payments/<str:user_id>/", GetUserPaymentsView.as_view()),
]
