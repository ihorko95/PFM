from manager.models import *
from django import template
register = template.Library()

@register.simple_tag(name = 'get_cats')
def get_categories():
    return Categories.objects.all()

@register.inclusion_tag('manager/categories_show.html')
def shows_categories(sort=None, cat_selected=2):
    cats = Categories.objects.order_by(sort)
    return {"cats": cats, 'cat_selected': cat_selected}
