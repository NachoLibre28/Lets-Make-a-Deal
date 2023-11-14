import random

name = input("Hey! What's your name? ")
print("Welcome " + name + "! I'm thinking of a number between 1 and 100")

my_number = random.randint(1, 100)
guesses = []
for guess_number in range(1, 11):
  valid_guess = False
  while not valid_guess:
    try: 
      user_guess = int(input("Take a guess...\n"))
      valid_guess = True
    except ValueError:
      print("Please provide a valid number.")
  difference = abs(my_number - user_guess)
  guesses.append(user_guess)

  if user_guess < my_number and difference > 10:
    print("Oops! Your guess is VERY low. Try again.")
  elif user_guess < my_number and difference < 10:
    print("Oops! Your guess is a BIT low. Try again.")
  elif user_guess > my_number and difference > 10:
    print("Oops! Your guess is VERY high. Try again.")
  elif user_guess > my_number and difference < 10:
    print("Oops! Your guess is a BIT high. Try again.")
  else:
    break

if user_guess == my_number:
  print("Good job " + name + "! You WON!" + " You guessed my number in " + str(guess_number) + " guesses!")
  print("Your guesses were: " + " ".join(str(x) for x in guesses))

else:
  print("Sorry " + name + ". You LOST. My number was " + str(my_number))

# test commit
