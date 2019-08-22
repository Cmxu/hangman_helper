import string

words = []

with open('words.txt', 'r') as file:
	for line in file:
		cword = line[:-1].lower()
		if cword.isalpha():
			words.append(cword)

def solver(pattern, used_letters):
	used_letters = list(used_letters)
	poss = [word for word in words if len(word) == len(pattern)]
	poss2 = []
	for word in poss:
		for i, letter in enumerate(word):
			if pattern[i] != '-':
				if pattern[i] != letter:
					break
			else:
				if letter in used_letters:
					break
		else:
			poss2.append(word)
	alpha = {l:len([word for word in poss2 if l  in word]) for l in string.ascii_lowercase}
	for letter in used_letters:
		alpha.pop(letter)
	guess = max(alpha, key = alpha.get)
	return guess, alpha, poss2

def play_game(word, lives):
	n = len(word)
	pattern = ['-' for _ in range(n)]
	used_letters = 'ae'
	for letter in used_letters:
		for i, let in enumerate(word):
			if let == letter:
				pattern[i] = let
	while lives > 0:
		guess = solver(''.join(pattern), used_letters)[0]
		used_letters += guess
		if guess in word:
			for i, let in enumerate(word):
				if let == guess:
					pattern[i] = guess
			if sum([i == '-' for i in pattern]) == 0:
				return True
		else:
			lives -= 1
	return False

def quick_entry():
	print('How many letters: ', end = '')
	n = int(input())
	turns = 26
	pattern = ['-' for _ in range(n)]
	used_letters = ''
	while turns > 0:
		turns -= 1
		a, b, c = solver(''.join(pattern), used_letters)
		print('You should guess ' + a)
		print(b)
		if len(c) < 10:
			print(c)
		print('What did you guess: ', end = '')
		g = input()
		print('Where: ', end = '')
		x = input()
		if x == '-1':
			used_letters += g
		else:
			used_letters += g
			sp = x.split(',')
			for s in sp:
				pattern[int(s)-1] = g	
	
