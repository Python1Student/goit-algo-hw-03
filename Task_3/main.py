import re

# Створюємо функцію для форматування номерів
def normalize_phone(phone_numbers: list) -> list:

    # Створюємо список в якому будуть готові номери
    formated_numbers = []
    

    # Перебираємо кожний номер з сирих номерів
    for phone_number in phone_numbers: 
        # Створюємо змінну зі значенням яке шукаємо а саме все окрім "+" та цифр
        pattern = r'[^\+\d]'
        # Створюємо змінну зі значенням на яке будемо заміняти
        replacement = r''

        # Видаляємо все з номера окрім "+" та цифр
        formated_number = re.sub(pattern, replacement, phone_number)

        # Перевіряємо чи перший символ "+"
        if formated_number[0] == '+':
            # Робимо данну операцію для того щоб залишити тільки один "+" якщо їх ненароком більше
            pattern = r'\D'
            formated_number = '+' + re.sub(pattern, replacement, phone_number)
        
        # Перевіряємо чи первші два символа не 38
        # Це потрібно для того якщо буде номер з кодом не 380 але вказаний +
        # То щоб програма не додавала лишнього
        if formated_number[:2] == '38':
            # Якщо так додаємо "+"
            formated_number = '+' + formated_number
        elif formated_number[0] != '+': 
            # Якщо ні і не вказано шо цей номер іншої країни то додаємо індекс України
            formated_number = '+38' + formated_number

        # Додаємо готовий номер в список
        formated_numbers.append(formated_number)
    
    # Повертаємо список
    if len(formated_numbers) == 1: return formated_numbers[0]
    else: return formated_numbers

# Отримуємо номер від користувача
phone_number = input('Input phone number: ')
print('Your formatted number:', normalize_phone([phone_number]))


# Можна розкоментувати для того щоб швидко перевірити
# Список номерів
# phone_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
#     '+8145-p = 2- 21763718', 
#     '+814w r695508315', 
#     '+380419442946', 
#     '+81166 4   r2549890', 
#     '+81620361119', 
#     '+3804171qfqf a asdf 87245', 
#     '+3806 2r 342 50421821', 
#     '+11033092187', 
#     '+38031231 t1rt  9221737', 
#     '+817261 r1r3g2325treg  420034']

# # Викликаємо та виводимо результат функції
# print('Your formatted numbers:', normalize_phone(phone_numbers))
