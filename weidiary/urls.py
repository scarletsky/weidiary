from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from diary.views import *
from registration.forms import RegistrationFormUniqueEmail
from weidiary import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', Index, name='diary_views_index'),
    url(r'^u/(?P<uid>\d{1,})/$', MonthDisplay, name='diary_views_month_display'),
    url(r'^u/(?P<uid>\d{1,})/(?P<month>\d{1,})/$', MyDiary, name='diary_views_mydiary'),
    url(r'^accounts/register/$', 'registration.views.register',
        {'form_class': RegistrationFormUniqueEmail,
         'backend': 'registration.backends.default.DefaultBackend'},       
         name='registration_register'),
	(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^privacy/$',Privacy, name='diary_views_privacy'),
    url(r'^service/$',Service, name='diary_views_service'),
    url(r'^about/$',About, name='diary_views_about'),
    url(r'^feedback/$',Feedback, name='diary_views_feedback'),
    # Examples:
    # url(r'^$', 'weidiary.views.home', name='home'),
    # url(r'^weidiary/', include('weidiary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
