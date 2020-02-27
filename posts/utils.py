from datetime import timedelta
from django.utils import timezone
from math import ceil
from re import findall


years = list(range(timezone.now().year-5, timezone.now().year+6))
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
days = list(range(1, 32))


def count_words(content):
    count = len(findall(r'\w+', content))
    return count


def get_read_time(content):
    words = count_words(content)
    time_in_min = round(words/200.0, 1)
    read_time = str(timedelta(minutes=time_in_min))
    return read_time
