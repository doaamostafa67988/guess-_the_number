from random import randint 
cp=randint(0,100)
counter=0
while True:
    
    try:
        user=int(input("enter number between 1 and 100 \n"))
    except ValueError:
        print("This is not a valid age.")
        continue
 
    counter+=1
    if cp==user:
        print('counter',counter)
        print('yes, you guess right')
        break
    elif cp < user:
        print('your guess is high')
        
    else:
        print(' your guess is low')
