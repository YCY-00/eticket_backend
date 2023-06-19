from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, DeleteView

User = get_user_model()


class UserDetailView(DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")


user_update_view = UserUpdateView.as_view()


class UserRedirectView(RedirectView):
    permanent = False


user_redirect_view = UserRedirectView.as_view()


class UserDeleteView(DeleteView):
    model = User
    fields = ["is_active"]
    success_message = _("User successfully deleted")


user_delete_view = UserDeleteView.as_view()
