from random import randint
n=randint(0,100)
print(n)
if n<30:
    print('Rainy')
elif n<60:
    print('Cloudy')
else:
    print('Sunny')