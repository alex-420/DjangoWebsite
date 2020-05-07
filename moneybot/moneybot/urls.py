from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Site wide navigation links, these links allow the user to navigate around the wite via navbar. made using class based views for efficiency and speed.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('posts/', include("posts.urls", namespace="posts")),
    path('forums/',include("forums.urls", namespace="forums")),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
]

urlpatterns += staticfiles_urlpatterns()
