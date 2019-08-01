from django import template

register = template.Library()

def get_item(dictionary,key):
    return dictionary.get(key)

register.filter('get_item',get_item)

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
#|cut:'hello'
register.filter('cut',cut)
