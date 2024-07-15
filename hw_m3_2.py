from random import sample

def get_numbers_ticket(min, max, quantity):

    if min<1:
        return []
    if max>1000:
        return []
    if min >=max:
        return []
    if (max - min) < quantity:
        return []
    return sorted(sample(range(min, max), quantity))
        
print("Ваші лотерейні числа:", get_numbers_ticket(10, 20, 11))