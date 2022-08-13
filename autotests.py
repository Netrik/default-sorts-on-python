import random

def create_test():
    numbers = []
    i = 0
    length = random.randint(1, 9999)
    while i < length:
        numbers.append(random.randint(-9999, 9999))
        i += 1
    return numbers