import re
import logging

from django import template

logger = logging.getLogger(__name__)
register = template.Library()

@register.tag(name="jsrequire")
def jsrequire(parse, token):
    """
        Syntax::
            {% jsrequire "<path_to_script>" [{arg}] %}

        Example::
            {% jsrequire "/widgets/receipt.js" 183.92 %}
    """
    # What is the tokens param???
    tokens = token.split_contents()
    if len(tokens) < 2:
        raise template.TemplateSyntaxError('Missing path to script. jsload')

    path = tokens.pop() #????????
    return JSRequireNode(path) # With no urls, this whole class can be removed???

class JSRequireNode(template.Node):
    def __init__(self, path):
        self.path = path

    def render(self, context):
        # Where does okonomi paths come from???
        if self.path and 'okonomi_paths' in context:
            # No need to 'resolve paths' since we're not doing urls
            resolved_path = self.resolve_template_variables(self.path, context)
            context['okonomi_paths'].append(resolved_path)
        return '<!-- requires %s -->' % (self.path or self.url)

    # !!!!!!!!!!!! Can probably remove this?? vvvvvvv !!!!!!!!!!!!!!
    def resolve_template_variables(self, path, context):
        """ Resolve any template variables in the path, it must be within double quotes.
            e.g. path `http://maps.google.com/maps?&key="{{ googlemaps_api_key }}"`
            becomes `http://maps.google.com/maps?&key=123`
        """
        template_vars = re.findall('"{{[a-zA-Z0-9\ _]+}}"', path)

        for v in template_vars:
            val = ''
            try:
                val = template.Variable(v.strip(' "{}')).resolve(context)
            except template.VariableDoesNotExist:
                logger.debug("Could not find template variable '%s' in context." % v)
            path = path.replace(v, val)

        return path
