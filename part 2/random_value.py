import random


def get_numbers_ticket(min=input("Enter minimal number from 1: \n"), max=input("Enter maximal number up to 1000: \n"), quantity=input("Enter quantity number, how long should be the list: \n")):

    min_int = int(min)
    max_int = int(max)
    quantity_int = int(quantity)

    pool_one = set()
    i = 0

    if min_int >= 1 and min_int < max_int:
        if max_int <= 1000 and max_int > min_int:
            if quantity_int <= max_int:
                while i < quantity_int:
                    number = random.randint(min_int, max_int)
                    pool_one.add(number)
                    if len(pool_one) < i+1:
                        i = i - 1
                    else:
                        i = i + 1
                num_list = list(pool_one)
                num_list.sort()
                return print(f'Ваші лотерейні числа: {num_list}')
            else:
                print(
                    "\n Quantity number should be bigger then 0, but not bigger then maximal number, try again\n")
        else:
            print("\n Maximal number should not be bigger then 1000 and not smaller then minimal number, try again\n")
    else:
        print("\n Minimal number should be bigger then 0, but not bigger then maximal number, try again\n")


get_numbers_ticket()
