import os
from django.conf import settings

STATIC_PATH = settings.JSLOAD_STATIC_PATH

def generate_js(paths):
    """given a list of javascript media paths, read
    them from disk and return their concatenation
    """
    if type(paths) == type(''):
        # TODO decrypt
        paths = paths.split('|')

    combined = ''
    for path in paths:
        # TODO use actual setting
        full_path = os.path.join(STATIC_PATH, path)
        with open(full_path, 'r') as f:
            combined += f.read()+'\n/* --- okonomi --- */\n' # TODO slurp file

    return combined
