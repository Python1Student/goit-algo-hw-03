from random import randint

# Створюємо функцію для виводу рандомних чисел
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    lotory_set = set()

    while len(lotory_set) < quantity:
        lotory_set.add(randint(min, max))
    
    return list(lotory_set)


# Робимо для того шоб потім нормально зупинити цикл
condition = True
# Пишемо за межами циклу шоб не повторювалося
print('''Enter tiket info: ''')

while condition:
    dict_input = {'min': None, 'max': None, 'quantity': None}

    for key in dict_input.keys():
        input_data = input(f'{key}: ')


        if not input_data.isdigit(): 
            print('Wrong input!')
            break


        dict_input[key] = int(input_data)

    if dict_input['min'] < 1 or dict_input['max'] > 1000 or dict_input['quantity'] > dict_input['max']:
        print('Wrong numbers!')
        continue
    
    print(get_numbers_ticket(**dict_input))
    condition = False
            