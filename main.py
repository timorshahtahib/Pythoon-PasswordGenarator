import string,random
#listcomperhencive
# nums=[num for num in range(10)]
# print(nums)



#odd number 
# nums=[num for num in range(10) if num%2==0] 
# print(nums)


while True:
    len=int(input("input your password lenghts :   "))
    chars=string.ascii_letters+string.digits+"@!#$%()"
    # text=[]
    # for i in range(len):
    #     text.append(random.choice(chars))
    # password="".join(text)
    # print("your password is :  {}".format(password))
    
    passs="".join([random.choice(chars) for i in range(len)])
    
   
    print("your password is :  {}".format(passs))
    
    while True:
        
        repet_again=input("dow you wanto repet aganin (Y/n)").lower()
        
        if repet_again=='n' or repet_again=='y':
            break
        

    if repet_again=='n':
        break
    
