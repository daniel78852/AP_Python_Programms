import random

print("***********Welcome***********\n")

dice_roll = random.randint(1, 6)
print("Test Dice: ", dice_roll)
user_input_dice = int(input("Guess a number between 1 and 6: "))

coin_tossed = ["H", "T"]
print("'H' for Heads, 'T' for Tails")
coin_toss = random.choice(coin_tossed)
print("Test Coin Toss: ", coin_toss)
coin_choice = input("What is your guess on the coin toss? 'H' for heads"
                    "'T' for tails? ").upper()


colors = ['R', 'Y', 'B', 'G']
print("What color would you like to bet on?"
                     "\n'r' for red \n'y' for Yellow,"
                     "\n'b' for Blue,\n'g' for green>>  ")

random_color = random.choice(colors)
print("Test random_colo",random_color)
color_choice = input("Color:  ").upper()

if user_input_dice == dice_roll and coin_choice == coin_toss and color_choice == random_color:
    print("\nYou win. Great job.")
    print(f'\nYour calls vs. Lady Luck,'
          f'\nDice: {user_input_dice} Ladyluck: {dice_roll}'
          f'\nCoin Toss: {coin_choice} ladyluck: {coin_toss}'
          f'\nColor Wheel: {color_choice} ladyluck: {random_color}')


elif user_input_dice == dice_roll and coin_choice == coin_toss or user_input_dice == dice_roll and color_choice == random_color or coin_toss == coin_choice and color_choice == random_color:
    print("\nGreat job you got 2 out of 3.")
    print("_______________________________________________________________________")
    print(f'\nYour calls vs. Lady Luck,'
          f'\nDice: {user_input_dice} Ladyluck: {dice_roll}'
          f'\nCoin Toss: {coin_choice} ladyluck: {coin_toss}'
          f'\nColor Wheel: {color_choice} ladyluck: {random_color}')

elif user_input_dice == dice_roll or coin_choice == coin_toss or color_choice == random_color:

    print("great call you got one right.")
    print("_______________________________________________________________________")
    print(f'\nYour calls vs. Lady Luck,'
          f'\nDice: {user_input_dice} Ladyluck: {dice_roll}'
          f'\nCoin Toss: {coin_choice} ladyluck: {coin_toss}'
          f'\nColor Wheel: {color_choice} ladyluck: {random_color}')

else:
    print("Sorry bud, you got none correctly. ")
    print("_______________________________________________________________________")
    print(f'\nYour calls vs. Lady Luck,'
          f'\nDice: {user_input_dice} Ladyluck: {dice_roll}'
          f'\nCoin Toss: {coin_choice} ladyluck: {coin_toss}'
          f'\nColor Wheel: {color_choice} ladyluck: {random_color}')

