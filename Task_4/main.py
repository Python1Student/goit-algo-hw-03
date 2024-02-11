from datetime import datetime, timedelta, date
from time import localtime, time
import os

os.system('cls')

# Створюємо функцію 
def get_upcoming_birthdays(users: list) -> list:
    # Створюємо два списки 
    # Один для днів народження які будуть за 7 днів і інший для тих які будут не скоро
    upcoming_birthdays, birthdays = [], []

    # Створюємо змінну today для того шоб позначити сьогоднішню дату
    today          = datetime.today().date()
    today_year_day = today.timetuple().tm_yday

    # Створюємо цикл в якому ми перебираємо кожний словник переданого списку 
    for user in users:
        # Присвоюємо значення ключа та його значення
        name, date_of_birth = list(user.items())[0]
        # Робимо з дати народження об'єкт datetime
        date_time_bd = datetime.strptime(date_of_birth, '%Y.%m.%d').date()
        # Створюємо змінну яка буде дорівнювати даті народження але цього року
        birthday          = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)
        birthday_year_day = birthday.timetuple().tm_yday

		# Перевіряємо чи вже було день народження
        if birthday_year_day - today_year_day in range(0, 8):
            while birthday.weekday() in (5, 6):
                birthday += timedelta(days=1)
            upcoming_birthdays.append({'name': name, 
                              'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})

        elif birthday_year_day - today_year_day > 7:
            birthdays.append({'name': name, 
                              'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})

        elif birthday_year_day - today_year_day < 0:
            birthdays.append({'name': name, 
                              'congratulating_date': datetime.strftime(birthday.replace(year=birthday.year+1), '%Y.%m.%d')})

    return upcoming_birthdays, birthdays


users = [
    {'Egor' : '2007.01.29'},
    {'Misha': '2010.02.17'}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print(f'Upcoming birthdays in 7 days: {upcoming_birthdays[0]}\nOther Birthdays: {upcoming_birthdays[1]}')