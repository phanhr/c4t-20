check = True
while check:
    txt=input("Enter your password: ")
    print(txt)
    for i in txt:
        if i.isdigit() and len(txt)>=8:
            check = False
            
    
        

            
