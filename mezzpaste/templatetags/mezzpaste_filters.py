from dpaste.highlight import LEXER_LIST
from mezzanine import template


register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    """Add the supplied CSS classes to the field, returning the HTML string."""
    return field.as_widget(attrs={"class": css})


@register.filter(name='lexer_display_name')
def get_lexer_display_name(snippet_lexer):
    """Return the Display Name of a Snippet's lexer."""
    lexers = LEXER_LIST[:2] + LEXER_LIST[2][1]
    for lexer in lexers:
        lexer_name = lexer[0]
        lexer_display_name = lexer[1]
        if lexer_name == snippet_lexer.strip():
            return lexer_display_name
