import sys
import random
import os
import time

#list of digits of a number
def getDigits(num):
	return [int(i) for i in str(num)]

#return true if number has no duplicates, else false.
def noDuplicates(num):
	num_li = getDigits(num)
	if len(num_li) == len(set(num_li)):
		return True
	else:
		return False

#generates 4 digit number, with no repeates
def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicates(num):
			return num
		
def countdown(t):
	while t > 0:
		print(t)
		t -= 1
		time.sleep(1)

def numOfBullsCows(num, guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)

	for i,j in zip(num_li,guess_li):
		if j in num_li:
			if j == i:
				#exact match.
				bull_cow[0] += 1
			else:
				#match, but not put in the right posistion.
				bull_cow[1] += 1
	return bull_cow


def main():
	num = generateNum()
	try:
		os.system('clear')
		tries = int(input('Enter number of tries: '))

		while tries > 0:
			guess = int(input(f'Guess numbers left: {tries}, Your Guess: '))
			if not noDuplicates(guess):
				print('''Number shouldn't have repeated digits, try again''')
				continue
			if guess < 1000 or guess > 9999:
				print('Enter only 4 digit numbers, try again.')
				continue
			
			bull_cow = numOfBullsCows(num,guess)
			print(f'{bull_cow[0]} bulls, {bull_cow[1]} cows')
			tries -=1

			if bull_cow[0] == 4:
				print("Congrats!")
				break
		else:
			print(f"You ran out of tries. Number was {num}")
	except:
		print('try again, it will start again in:')
		countdown(t=5)
		main()


if __name__ == '__main__':
	main()