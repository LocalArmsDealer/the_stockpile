# Imports
import random as r

# Main Menu
print("""Minigames by LocalArmsDealer
1. Russian Roulette
2. Chess
3. Go Fish
Email allinglin103@gmail.com for game suggestions.""")
game_chosen = input("Pick a game:")
if game_chosen = 1:
    ru_roul()
elif game_chosen = 2:
    chess()
elif game_chosen = 3:
    go_fish()
else:
    print("Error 1.")

# Russian Roulette
def ru_roul():
    bullet = r.randint(1,6)
    input = int(input("Pick a number between 1 and 6."))
    if input == bullet and input >= 1 and input <= 6:
        print("You died.")
    elif input != bullet and input >= 1 and input <= 6:
        print("You lived.")
    else:
        print("Error 2.")

# Chess
def chess():
    print("In development 1.")

# Go fish
def go_fish():
    print("In development 2.")
