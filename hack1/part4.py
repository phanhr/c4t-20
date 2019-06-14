a=input('username: ')
check = True
while check:
    b=input('password(co chu,so, lon hon 8 ky tu): ')
    for i in b:
        if i.isdigit and i.isalpha and len(b)>8:
            check=False
while True:
    d=input('nhap lai mat khau: ')
    if d==b:
        print('nhap mat khau thanh cong')
        break
    else:
        print('mat khau khong khop')
while True:
    c=input('email: ')
    if '@gmail.com' in c:
        print('Email hop le')
        break
    else:
        print('Email khong hop le')

print('dang ki thanh cong!')
print(a,b,c)