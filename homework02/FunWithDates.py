# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import date, timedelta, datetime

dt_today = date.today()
delta_1d = timedelta(days = 1)
dt_yesterday = dt_today - delta_1d
dt_month_ago = date(dt_today.year, dt_today.month - 1, dt_today.day)

print("Today is " + dt_today.strftime('%Y.%m.%d'))
print("Yesterday was " + dt_yesterday.strftime('%Y.%m.%d'))
print("One month ago it was " + dt_month_ago.strftime('%Y.%m.%d'))

date_string = "01/01/17 12:10:03.234567"
dt_result = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print(dt_result)