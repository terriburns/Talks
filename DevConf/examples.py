import random

number = random.randint(1, 10)
guess = raw_input('Guess a number 1-10. If you\'re right, you win a million bucks: ')

#convert strings to integers
def convert(wordString):
  if(wordString == 'one'):
    return 1
  elif(wordString == 'two'):
    return 2
  else:
    return 3

#if needed, convert strings to integers
if(isinstance(guess, str)):
  guess = convert(guess)

#check the guesses
if (guess > 10):
  print("Make sure your guess is between 1 and 10, inclusive")
elif (guess == number):
  print("Omg, you win a million bucks! Ask someone in the audience for it.")


