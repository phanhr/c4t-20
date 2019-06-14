print("hello world")
a=int(input(" nhap a: "))
b=int(input(" nhap b: "))
c=int(input(" nhap c: "))
y=b*b-4*a*c
if y>0: 
    print ('nghiem cua pt la:x1=',(-b+y**0.5)/(2*a),'hoac x2=',(-b-y**0.5)/(2*a))
elif y==0:
    print ('nghiem cua pt la: x1=x2=',-b/(2*a))
else:
    print ('phuong trinh vo nghiem')