import re


def normalize_phone(phone_number: str) -> str:

    pattern = r'\D'
    replacement = r''
    formated_number = re.sub(pattern, replacement, phone_number)

    ukraine_index = '380'
    find_ukraine_index = re.search(ukraine_index, formated_number)
    
    if find_ukraine_index.span == (0, 3):
        formated_number = '+' + formated_number
    else: formated_number = '+38' + formated_number
    
    return formated_number


# Робимо для того шоб потім нормально зупинити цикл
condition = True
# Пишемо за межами циклу шоб не повторювалося
print('Enter phone number: ')

while condition:
    phone_number = input('>>> ')

    print(normalize_phone(phone_number))
