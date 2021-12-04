import random 
number=random.randint(1,9)
chances=5
print("The Number Guessing Game!")
print("Guess a number between 0 and 9")
while(chances>0):
    chances=chances-1
    answer=int(input("Enter your Guess:"))
    if(answer==number):
        print('Your answer is correct. YOU WIN!')
        break
    elif(answer<number):
        print('Your guess is lower than the number, Guess again')
    elif(answer>number):
        print('Your guess is greater than the number, Guess again')
if(chances==0):
        print('YOU LOSE!! The number is',number)