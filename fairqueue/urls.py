"""fairqueue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django.conf import settings

from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.home, name='home'),
    # path('adminapp/', include('adminapp.urls')),
    path('accounts/', include('signupapp.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    # Django Admin
    re_path(r'^{}/'.format('admin'), admin.site.urls),  # settings.DJANGO_ADMIN_URL -> admin/
)

# from django.contrib.auth import views as auth_views
#
# order is important, must be before ...format('accounts') to avoid redirect to pasword_change_done
# urlpatterns += i18n_patterns(
# path(
#         'accounts/password_change/',
#         auth_views.PasswordChangeView.as_view(success_url='/'),
#         name='password_change'
#     ),
# )

urlpatterns += i18n_patterns(
    # login, change and reset pwd
    re_path(r'^{}/'.format('accounts'), include('django.contrib.auth.urls')),
)
urlpatterns += i18n_patterns(
    # adminapp
    re_path(r'^{}/'.format('adminapp'), include('adminapp.urls')),
)