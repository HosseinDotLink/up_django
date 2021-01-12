from django import template

register = template.Library()

@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None

@register.filter
def return_user_data(l,i):
    try:
        user_data = l[i][0].username + " - " + l[i][0].first_name + " " + l[i][0].last_name
        return user_data
    except:
        return None

@register.filter
def return_user_data_no_username(l,i):
    try:
        user_data = l[i][0].first_name + " " + l[i][0].last_name
        return user_data
    except:
        return None