from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# Misaka is used to allow for html markdown in posts
import misaka

# Gets current user modlogged into the site and assigns it to 'User'
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# This class will return database records for the forums app, the fields have been selected for maximum user enjoyment.
class Forum(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    info = models.TextField(blank=True, default='')
    info_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="ForumMember")

    def __str__(self):
        return self.name

    # Save method for new forums created, slug is used to create an addressable URL. this can then be sent to others and bookmarked for ease of use.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.info_html = misaka.html(self.info)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forums:single", kwargs={"slug": self.slug})

    # Forums will be sorted by name when returned
    class Meta:
        ordering = ["name"]

# Class returns which user is a member of which forum
class ForumMember(models.Model):
    forum = models.ForeignKey(Forum,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_forums',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("forum", "user")
