import datetime
import bday_message

# Fecha de tu próximo cumpleaños
birth_month = 7
birth_day = 18
today = datetime.date.today()
current_year = today.year

# Fecha del cumpleaños en el año actual
next_birthday = datetime.date(current_year, birth_month, birth_day)

# Si ya pasó este año, usa el próximo año
if today > next_birthday:
    next_birthday = datetime.date(current_year + 1, birth_month, birth_day)

# Calcula los días entre hoy y el próximo cumpleaños
days_away = (next_birthday - today).days

# Verifica si hoy es tu cumpleaños
if today.month == birth_month and today.day == birth_day:
    print(bday_message.random_message)
else:
    print(f'My next birthday is {days_away} days away!')