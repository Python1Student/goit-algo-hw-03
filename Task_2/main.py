from random import randint

# Створюємо функцію для виводу рандомних чисел
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # Створюємо множину щоб були тільки унікальні числа
    lotory_set = set()

    # Використовуємо саме так бо одна і та сама цифра може попастися двічі 
    # а множина її не зарахує тому робимо пока довжина менше кількості цифр
    while len(lotory_set) < quantity:
        # Додаємо рандомне число в заданому діапазоні
        lotory_set.add(randint(min, max))
    
    # З множини робимо список та повертаємо
    return list(lotory_set)


# Робимо для того шоб потім нормально зупинити цикл
condition = True
# Пишемо за межами циклу шоб не повторювалося
print('Enter tiket info: ')

# Цикл для того щоб програма не закінчувалася при вводі не правильних данних
while condition:
    # Створюємо словник в циклі щоб якщо ввели не так то неправильні значення зникли
    dict_input = {'min': None, 'max': None, 'quantity': None}

    # Цикл для заповнення словника
    for key in dict_input.keys():
        # Отримуємо значення з клавіатри
        input_data = input(f'{key}: ')

        # Перевіряємо чи введено число якщо ні присвоюємо 0
        dict_input[key] = int(input_data) if input_data.isdigit() else 0

    # Перевіряємо числа чи підходять вони по критеріям
    if (dict_input['min'] < 1 or 
        dict_input['max'] > 1000 or 
        dict_input['quantity'] > dict_input['max'] or 
        dict_input['min'] > dict_input['max']):
        print('Wrong numbers!')
        continue
    
    # Викликаємо функцію і воводим її результат
    print(get_numbers_ticket(**dict_input))
    # Ставимо False щоб програма більше не повторювалася
    condition = False
            