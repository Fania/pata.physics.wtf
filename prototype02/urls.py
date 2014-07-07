from django.conf.urls.defaults import *
from prototype02.views import main, results

urlpatterns = patterns('',
    ('^prototype02/results/$', results),
    ('^prototype02/$', main),
    #('^time/$', current_datetime),
    #('^another-time-page/$', current_datetime),
    #(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
