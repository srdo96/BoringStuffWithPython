import random

pcGuess = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.\nGuess my number with in 3 chances')
flag = 0
for i in range(1,4):
	print('Take a guess.')
	playerGuess = int(input())
	if pcGuess == playerGuess:
		print('Good job! You guessed my number in ' + str(i) + ' guesses!')
		flag = 1
		break
	elif pcGuess - playerGuess > 0:
		print('Your guess is too low.')
	else:
		print('your guess is too high')

if flag == 0:
	print("Sorry! Your limit is over. The number I was thinking of was " +
	 str(pcGuess))	
