from django.conf.urls.defaults import patterns, url

from jsload.views import OkonomiJavascript

urlpatterns = patterns('',
    url(r'^(?P<combined_path>.+)$', OkonomiJavascript.as_view()),
)
