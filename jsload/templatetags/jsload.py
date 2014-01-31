from django import template
from TagNode import TagNode

register = template.Library()

@register.tag(name="jsload")
def jsload(parse, token):
    """
        Syntax::
            {% jsload "<path_to_script>" [{arg}] %}

        Example::
            {% jsload "/widgets/receipt.js" 183.92 %}
    """
    tokens = token.split_contents()
    try:
        path = tokens[1]
    except IndexError:
        raise template.TemplateSyntaxError('Missing path to script.')

    arguments = tokens[2:]
    return TagNode(path, arguments)
