from django.conf import settings

JS_PLACEHOLDER = '${JSREQUIRE}'
STATIC_URL = settings.JSLOAD_STATIC_URL
HTML_TEMPLATE = '<script async src="%s"></script>'

# What is object??????
class JSLoad(object):
    """
    The okonomi middleware prepares unique combinations of javascript includes
    for rendered django templates. It stores the combined javascript in memcache
    for fast serving by a view used as a single point of javascript inclusion.
    """

    def process_request(self, request):
        request.jsload_paths = []

    def process_response(self, request, response):
        script = ''
        included_paths = []

        try:
            all_paths = request.jsload_paths
        except AttributeError:
            all_paths = []

        # Add each script once, skipping subsequent duplicates.
        for path in all_paths:
            if path not in included_paths:
                included_paths.append(path)
                url = STATIC_URL + path
                script += (HTML_TEMPLATE % url)

        # Cast to string to avoid possible UnicodeDecodeErrors.
        script_str = str(script)
        response.content = response.content.replace(JS_PLACEHOLDER, script_str)
        return response

def context_processor(request):
    """ Stick paths collection into the template context. """
    try:
        context = {
            'jsload_paths': request.jsload_paths
        }
    except AttributeError:
        context = {}
    return context
