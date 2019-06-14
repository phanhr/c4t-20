from turtle import *
n=int(input("nhap so canh: "))
angle=360//n
for i in range(n):
    forward(100)
    right(angle)
mainloop()
print('hello')