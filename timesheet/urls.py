from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ts_app import views

urlpatterns = [
    re_path(r'^$', login_required(views.entry.IndexView.as_view()), name='entry'),

    re_path(r'^employee/$', login_required(views.employee.IndexView), name='employee'),
    re_path(r'^ajax/validate_username/$', login_required(views.validate_username), name='validate_username'),

    re_path(r'^project/$', login_required(views.project.IndexView), name='project'),

    re_path(r'^client/$', login_required(views.client.IndexView), name='client'),
    re_path(r'^report/$', login_required(views.report.IndexView), name='report'),

    re_path(r'^admin/', admin.site.urls, name="admin"),
    # re_path(r'^login/$', auth_views.login, {'template_name': 'employee_login.html'}, name='login'),
    # re_path(r'^logout/$', login_required(auth_views.logout), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
