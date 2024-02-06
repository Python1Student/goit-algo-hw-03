import re
from datetime import datetime

# Створюємо функцію для обчислення кількості днів між датами
def get_days_from_today(date):
    pass

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