import random 
from fruits import fruits

fruit = random.choice(fruits)
chances = len(fruit) + 3
guessAdd = []
done = False

while not done:
    for letter in fruit:
        if letter.lower() in guessAdd:
            print(letter, end= " ")
        else:
            print("-", end= "")
    userGuess = input(f"Your chances is {chances}, Guess the letter: ")
    guessAdd.append(userGuess.lower())

    if userGuess.lower() not in fruit.lower():
        chances -= 1
        if chances == 0:
            break
    done = True
    for letter in fruit:
        if letter.lower() not in guessAdd:
            done = False

if done: 
    print(f"Yes, you have won the game, the word is {fruit}")
else:
    print("you loss the game")
    print("The random word is: ",fruit)


