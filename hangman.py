import random

# Banner
print(''' _                                             _ 
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
| '_  \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\| |
| | | | (_| | | | | (_| | | | | | | (_| | | | |_|
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_(_)
                   |___/                         ''')

# Word list and random selection
words = ['apple', 'mango', 'banana', 'lime', 'orange']
word = random.choice(words)

# Game variables
game=['_']*len(word)
lives=6
def mass(game,x,word):
    found=False
    for i in range(len(word)):
        if ((word[i])==x):
            game[i] = x
            found=True
    return found
while lives>0:
    print("Current word: " + " ".join(game))
    x=input("enter the letter").lower()
    if len(x) != 1 or not x.isalpha():
        print("Please enter a single valid letter.")
        continue
    if x in game:
        print(f"You already guessed '{x}'. Try a different letter.")
        continue
    y=mass(game,x,word)
    if y==1:
        print("Correct guess!")
    else:
        lives=lives-1
        if(lives==6):
            print(''' +---+
       |
       |
       |
      ===''')
        elif(lives==5):
            print(''' +---+
   O   |
       |
       |
      ===''')
        elif(lives==4):
            print('''+---+
   O   |
   |   |
       |
      ===''')
        elif(lives==3):
           print(''' +---+
   O   |
  /|   |
       |
      ===''')
        elif(lives==2):
            print('''  +---+
   O   |
  /|\\  |
       |
      ===''')
        elif(lives==1):
            print(''' +---+
   O   |
  /|\\  |
  /    |
      ===''')
        print(f"remainig lifes are{lives}")
    if "_" not in game:
        print("Congratulations! You guessed the word:", "".join(game))
        break
else:
    print(f"Game over! The word was: {word}")
    print('man died')
    print('''+---+
   O   |
  /|\\  |
  / \\  |
      ===''')

