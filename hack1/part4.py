name=input('username: ')
check = True
while check:
    password=input('password(co chu,so, lon hon 8 ky tu): ')
    for i in password:
        if i.isdigit and i.isalpha and len(password)>8:
            check=False
while True:
    repass=input('nhap lai mat khau: ')
    if repass==password:
        print('nhap mat khau thanh cong')
        break
    else:
        print('mat khau khong khop')
while True:
    Email=input('email: ')
    if "@" in Email and "." in Email:
        print('Email hop le')
        break
    else:
        print('Email khong hop le')

print('dang ki thanh cong!')
print(name,password,Email)