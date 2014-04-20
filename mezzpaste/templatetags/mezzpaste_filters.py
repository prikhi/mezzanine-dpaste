from django import template


register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    """Add the supplied CSS classes to the field, returning the HTML string."""
    return field.as_widget(attrs={"class": css})
