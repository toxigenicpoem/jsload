from django.core.cache import cache
from django.http import Http404, HttpResponse
from django.views.generic.base import View

# TODO good cache headers

class OkonomiJavascript(object):
    """
    OkonomiJavascript serves combined javascript files from cache, regenerating
    them if necessary.
    """

    def get(self, *args, **kwargs):
        try:
            combined_path = kwargs['combined_path']
        except KeyError, e:
            logging.error('malformed request for javascript: %s' % e)
            raise Http404('Combined script not found.')

        cache_key = 'jsload:%s' % combined_path
        js = cache.get(cache_key)
        if js is None:
            js = okonomi.utils.generate_js(combined_path)

        cache.set(cache_key, js)

        return HttpResponse(js, mimetype="text/javascript")
