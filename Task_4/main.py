from datetime import datetime, timedelta, date
from time import localtime, time
import os

# Для того щоб не було видно попередні виклики програми
os.system('cls')

# Створюємо функцію 
def get_upcoming_birthdays(users: list) -> list:
    # Створюємо два списки 
    # Один для днів народження які будуть за 7 днів і інший для тих які будут не скоро
    upcoming_birthdays, birthdays = [], []

    # Створюємо змінну today для того шоб позначити сьогоднішню дату
    today          = datetime.today()
    # І змінну today_year_day щоб позначити який сьогодні день в цьому році
    today_year_day = today.timetuple().tm_yday

    # Створюємо цикл в якому ми перебираємо кожний словник переданого списку 
    for user in users:
        # Присвоюємо значення ключа та його значенняx
        name, date_of_birth = list(user.values())
        # Робимо з дати народження об'єкт datetime
        date_time_bd = datetime.strptime(date_of_birth, '%Y.%m.%d')
        # Створюємо змінну яка буде дорівнювати даті народження але цього року
        birthday          = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)
        # Отримуємо день року коли день народженя
        birthday_year_day = birthday.timetuple().tm_yday
        
        # Поки дата є субота або неділя ми переносимо дату на 1 день
        while birthday.weekday() >= 5:
            birthday += timedelta(days=1)

		# Перевіряємо чи не є день народження в найближчі 7 днів
        if birthday_year_day - today_year_day in range(0, 8): 
            # Додаємо дату привітання
            upcoming_birthdays.append({
                'name': name, 
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
                })

        # Перевіряємо чи вже буде день народження в цьому році
        elif birthday_year_day - today_year_day > 7:
            # Додаємо дату привітання
            birthdays.append({
                'name': name, 
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
                })
            
        # Перевіряємо чи вже було день народження
        else:
            # Додаємо дату привітання
            birthdays.append({
                'name': name, 
                'congratulating_date': datetime.strftime(birthday.replace(year=birthday.year+1), '%Y.%m.%d')
                })

    # Повертаємо два списки
    return upcoming_birthdays, birthdays

# Створюємо список робітників
users = [
    {'name': 'Egor', 'birthday' : '2007.01.30'},
    {'name': 'Misha', 'birthday': '2010.02.17'},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.25"}
]

# Створюємо два списка один для днів народження які скоро інший для інших
upcoming_birthdays, birthdays = get_upcoming_birthdays(users)

# Виводимо в консоль результат
print(f'Upcoming birthdays in 7 days: {upcoming_birthdays}\nOther Birthdays: {birthdays}')