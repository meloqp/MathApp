import random

def output(low_border, high_border, num_of_slag):
    l = []
    l.append(random.randint(low_border, high_border))
    for i in range(num_of_slag-1):
        l.append(random.randint(low_border, high_border))
    return str(l)
