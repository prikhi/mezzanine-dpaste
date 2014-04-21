from django.db.models import Count
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
