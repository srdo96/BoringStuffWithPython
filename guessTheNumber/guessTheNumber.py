import random

print('I am thinking of a number between 1 and 20.')
pcGuess = random.randint(1, 20)
i = 1
while True:
	print('Take a guess.')
	playerGuess = int(input())
	if pcGuess == playerGuess:
		print('Good job! You guessed my number in ' + str(i) + ' guesses!')
		break
	elif pcGuess - playerGuess > 0:
		print('Your guess is too low.')
	else:
		print('your guess is too high')
	i = i + 1
