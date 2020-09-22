from django import template
register = template.Library()

@register.filter
def paid_amount(value, item):
	return value[item]
