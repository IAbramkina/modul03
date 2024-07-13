from random import sample

def get_numbers_ticket(min, max, quantity):

    if min<1:
        return []
    if max>1000:
        return []
    if min >=max:
        return []

    return sorted(sample(range(min, max), quantity))
        
print("Ваші лотерейні числа:", get_numbers_ticket(1, 10, 5))