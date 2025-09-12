import random

signs_list = ["+", "/", "-", "*"]

def output(low_border, high_border, num_of_slag):
    num_list = list()
    for i in range(num_of_slag-1):
        num_list.append(random.randint(low_border, high_border))
        num_list.append(signs_list[random.randrange(len(signs_list))])
    num_list.append(random.randint(low_border, high_border))
    return "".join(list(map(str, num_list)))


