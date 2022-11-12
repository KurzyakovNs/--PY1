import random
symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def get_random_password(n=8):
    password = ''.join(random.sample(symbol,n))
    return password

print(get_random_password(6))
