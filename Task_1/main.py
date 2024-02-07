from datetime import datetime, timedelta

# Створюємо функцію для обчислення кількості днів між датами
def get_days_from_today(date: str) -> None:
    # Перетворюємо рядок в обьєкт datetime
    date_time = datetime.strptime(date_input, '%Y-%m-%d')
    # Задаємо сьогоднішню дату
    date_today =  datetime.today()
    
    # Рахуємо скільки днів між двома датами
    result = abs(date_today.toordinal() - date_time.toordinal())

    # Виводимо відповідь
    print(f'The difference between {date_time.strftime('%d %B %Y')} and today\'s date is {result} days')

# Робимо для того шоб потім нормально зупинити цикл
condition = True
# Пишемо за межами циклу шоб не повторювалося
print('Write date in format: YYYY-MM-DD')

while condition:
    # Отримуємо ввод з клавіатури
    date_input = input('>>> ')

    # Перевіряємо чи правильно ввів користувач дату
    try: datetime.strptime(date_input, '%Y-%m-%d')
    except: 
        print('Wrong date!')
        continue
    
    # Ставимо False шоб більше не повторювався цикл перевірки
    condition = False
    # Нарешті викликаємо функцію для обчислення
    get_days_from_today(date_input)