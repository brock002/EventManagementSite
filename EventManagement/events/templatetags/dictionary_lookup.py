from django import template

register = template.Library()

@register.filter(name='dictlookup')
def dictionary_variable_lookup(value, arg):
    return value[arg]