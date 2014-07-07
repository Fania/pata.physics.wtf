from django.conf.urls.defaults import *
from prototype01.views import main, results

urlpatterns = patterns('',
    ('^prototype01/results/$', results),
    ('^prototype01/$', main),
    #('^time/$', current_datetime),
    #('^another-time-page/$', current_datetime),
    #(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
