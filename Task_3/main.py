import re


def normalize_phone(phone_numbers: list) -> list:

    formated_numbers = []

    for phone_number in phone_numbers:
        pattern = r'[^\+\d]'
        replacement = r''
        formated_number = re.sub(pattern, replacement, phone_number)

        if formated_number[0] == '+':
            pattern = r'\D'
            formated_number = '+' + re.sub(pattern, replacement, phone_number)
        
        if formated_number[:2] == '38':
            formated_number = '+' + formated_number
        elif formated_number[0] != '+': 
            formated_number = '+38' + formated_number
            # print(find_ukraine_index)

        formated_numbers.append(formated_number)
        
    return formated_numbers


phone_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    '+8145-p = 2- 21763718', 
    '+814w r695508315', 
    '+380419442946', 
    '+81166 4   r2549890', 
    '+81620361119', 
    '+3804171qfqf a asdf 87245', 
    '+3806 2r 342 50421821', 
    '+11033092187', 
    '+38031231 t1rt  9221737', 
    '+817261 r1r3g2325treg  420034']

print(normalize_phone(phone_numbers))
