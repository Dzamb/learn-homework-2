"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")

def print_days():
    date_today = datetime.now()
    date_yesterday = date_today - timedelta(1)
    date_month_ago = date_today - timedelta(30)
    print(f"Сегодня: {date_today.strftime('%A %d %B %Y')}")
    print(f"Вчера: {date_yesterday.strftime('%A %d %B %Y')}")
    print(f"Месяц назад: {date_month_ago.strftime('%A %d %B %Y')}")

    
    
def str_2_datetime(string):
    date_string = "01/01/17 12:10:03.234567"
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
