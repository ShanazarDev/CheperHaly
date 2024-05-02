from django import template
from ..models import HomeBackgroundModel

register = template.Library()


@register.inclusion_tag('en/../../templates/background.html')
def back_home(lg: bool = False, section: bool = False):
    back = HomeBackgroundModel.objects.last()

    if back:
        if lg and section:
            return {'back': back, 'lg': lg, 'section': section}
        else:
            return {'back': back, 'lg': lg, 'section': section}
    else:
        return {'None': None, 'section': section}
