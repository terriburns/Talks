import random

number = random.randint(1, 10)
while True:
  try:
    guess = int(input('Guess a number 1-10. If you\'re right, you win a million bucks: '))
    #print(guess)
    #print(number)
    break
  except NameError:
    print("Oops! Make sure you enter a number, not a word.")

#check the guesses
if (guess > 10 or guess < 1):
  print("Make sure your guess is between 1 and 10, inclusive")
elif (guess == number):
  print("Omg, you win a million bucks! Ask someone in the audience for it.")
else:
  print("awk, loser.")


