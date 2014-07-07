from django.conf.urls.defaults import *
from prototype03.views import main, results

urlpatterns = patterns('',
    ('^prototype03/results/$', results),
    ('^prototype03/$', main),
    #('^time/$', current_datetime),
    #('^another-time-page/$', current_datetime),
    #(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
