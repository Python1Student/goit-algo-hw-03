import re


def normalize_phone(phone_number: str) -> str:

    pattern = r'\D'
    replacement = r''
    formated_number = re.sub(pattern, replacement, phone_number)
    formated_number = '+' + formated_number
    
    return formated_number


# Робимо для того шоб потім нормально зупинити цикл
condition = True
# Пишемо за межами циклу шоб не повторювалося
print('Enter number: ')

while condition:
    phone_number = input('>>> ')

    print(normalize_phone(phone_number))
