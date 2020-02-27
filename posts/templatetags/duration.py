from django import template

register = template.Library()


@register.filter
def etr(value):
    splitted = value.split(':')

    hours = int(splitted[0])
    minutes = int(splitted[1])

    if hours == 0:
        if minutes < 1:
            return f"less than 1 minute"
        elif minutes == 1:
            return f"1 minute"
        elif 5 > minutes > 1:
            return f"less than 5 minutes"
        else:
            return f"{minutes} minutes"
    elif hours < 2:
        if not minutes:
            return f"{hours} hour"
        elif minutes < 2:
            return f"{hours} hour, {minutes} minute"
        else:
            return f"{hours} hour, {minutes} minutes"
    else:
        if not minutes:
            return f"{hours} hours"
        elif minutes < 2:
            return f"{hours} hours, {minutes} minute"
        else:
            return f"{hours} hours, {minutes} minutes"
