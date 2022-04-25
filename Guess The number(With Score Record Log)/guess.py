import random

print("Welcome to 'Guess the number' game!")

num = random.randint(1,50)
guess = 0
while True:
    user = int(input("Enter the number: "))
    if user > num:
        print("Enter a smaller number")
    elif user <num:
        print("Enter a larger number.")        
    else:
        print("You won!")
        break
    guess = guess+1
print("You took", guess,"number of guesses!")

with open ("Highscore.txt") as f:
    score = f.read()
    if str(score) > str(guess):
        with open ("Highscore.txt", "w") as f:
            highscore = f.write(str(guess))









