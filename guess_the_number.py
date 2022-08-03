cp=randint(0,100)
counter=0
while True:
    counter+=1
    user=int(input("enter number between 1 and 100 \n"))
    if cp==user:
        print('counter',counter)
        print('yes, you guess right')
        break
    elif cp < user:
        print('your guess is high')
        
    elif cp > user:
        print(' your guess is low')
