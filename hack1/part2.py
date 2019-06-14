for i in range(3,13):
    print(i)
n=int(input('nhap so n>0: '))
for b in range(0,n+1):
    print(b)
m=int(input('nhap so m>0: '))
while m>=0:
    if m%2==1:
        print(m)
    m-=1
from turtle import *
n=int(input("nhap so canh: "))
angle=360//n
for i in range(n):
    forward(100)
    right(angle)
mainloop()

