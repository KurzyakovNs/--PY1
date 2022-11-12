import random
def get_unique_list_numbers():
    str_ = []
    i = 0
    while i != 15:
        a = random.randint(-10,10)
        if a not in str_:
            str_.append(a)
            i+=1
    return(str_)

list_unique_numbers = get_unique_list_numbers()
print(get_unique_list_numbers())
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
