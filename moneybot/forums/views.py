from django.contrib import messages
from django.contrib.auth.mixins import(LoginRequiredMixin,PermissionRequiredMixin)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from forums.models import Forum,ForumMember
from . import models

#Class based views have been used in this app allowing for speed and efficiency.

# new forum class
class CreateForum(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "info")
    model = Forum

# View one forum
class SingleForum(generic.DetailView):
    model = Forum

#View all forums
class ListForums(generic.ListView):
    model = Forum

# Class to join a forum.
class JoinForum(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("forums:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        forum = get_object_or_404(Forum,slug=self.kwargs.get("slug"))

        try:
            ForumMember.objects.create(user=self.request.user,forum=forum)

        except IntegrityError:
            messages.warning(self.request,("Are you sure? You're already a member of {}".format(forum.name)))

        else:
            messages.success(self.request,"You are now a member of the {} forum.".format(forum.name))

        return super().get(request, *args, **kwargs)


class LeaveForum(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("forums:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.ForumMember.objects.filter(
                user=self.request.user,
                forum__slug=self.kwargs.get("slug")
            ).get()

        except models.ForumMember.DoesNotExist:
            messages.warning(
                self.request,
                "You are not part of this forum."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "Successfully left this forum."
            )
        return super().get(request, *args, **kwargs)
