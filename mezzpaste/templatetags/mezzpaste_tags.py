from django.db.models import Count
from django.conf import settings
from dpaste.models import Snippet
from mezzanine import template


register = template.Library()


@register.as_tag
def mezzpaste_stats(limit=5):
    """
    Put a list of the top Lexers used into the template context.

    Usage::

        {% mezzpaste_stats 5 as top_lexers %}

    """
    top_lexers = Snippet.objects.values('lexer').annotate(
        count=Count('lexer')).order_by('-count')
    return list(top_lexers[:limit])


@register.simple_tag
def mezzpaste_pygments_css_class():
    """Return the Pygments CSS Class Specified in the Settings module."""
    return settings.MEZZPASTE_PYGMENTS_CSS
