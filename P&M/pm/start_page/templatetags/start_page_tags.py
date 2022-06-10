from django import template
from ..forms import Search

register = template.Library()

@register.simple_tag(name='search_form')
def add_search():
    return Search()