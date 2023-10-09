from random import randint

x = randint (1, 10)
#print(x)
user_num = 0
attempt = 0 

while True:
    print (' Guess a number from 1 to 10')
    user_num = int(input("Your guess:"))
    attempt += 1
    if user_num == x:
        print(" Well done!\nAmount of attempts:"+str(attempt) + " \nThanks for playing!")
        break
    elif user_num > x:
        print(" The number is smaller than this.")
    elif user_num < x:
        print(" The number is bigger than this.")  
        
         