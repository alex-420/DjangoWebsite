from django.contrib import admin
from . import models
# Custom admin heading to help the admin user navigate.
admin.site.register(models.Forum)
admin.site.site_header = 'MoneyBot Admin Dashboard'

class ForumMemberInline(admin.TabularInline):
    model = models.ForumMember
