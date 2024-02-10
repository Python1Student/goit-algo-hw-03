from datetime import datetime, timedelta

# Створюємо функцію 
def get_upcoming_birthdays(users: list) -> list:
    # Створюємо два списки 
    # Один для днів народження які будуть за 7 днів
    upcoming_birthdays = []
    # Інший для тих які будут не скоро
    birthdays = []

    # Створюємо змінну today для того шоб позначити сьогоднішню дату
    today = datetime.today().date()

    # Створюємо цикл в якому ми перебираємо кожний елемент переданого списку 
    for user in users:
        key, value = user
        date_time_bd = datetime.strptime(value, '%Y.%m.%d').date()
        birthday = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day).date()

        if birthday < today:
            birthdays.append({'name': key, 'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})
        elif birthday.toordinal() - today.toordinal() <= 7:
            while birthday.weekday() in (5, 6):
                birthday += timedelta(days=1)
            upcoming_birthdays.append({'name': key, 'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')})
    
    return upcoming_birthdays, birthdays


users = [
    {'Egor': '2007.02.04'},
    {'Misha': '2010.02.10'}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print(f'Upcoming birthdays in 7 days: {upcoming_birthdays[0]}\nOther Birthdays: {upcoming_birthdays[1]}')