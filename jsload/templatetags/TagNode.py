import re
from django import template

class TagNode(template.Node):
    def __init__(self, path, arguments):
        self.path = path
        self.arguments = arguments

    def render(self, context):
        msg = self.path
        for key in self.arguments:
            value = context[key]
            msg += ', %s=%s' % (key, value)
        return '~~%s~~' % msg


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
