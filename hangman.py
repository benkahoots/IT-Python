import time
import random

print "Welcome to Ben Tegoni's Hang-Man Game!"
time.sleep(1)
print ""

print "All answers and guesses must be in lower case form!"
time.sleep(1)
print ""

print "Are you playing with two people? Answer yes or no."
players = raw_input()
time.sleep(1)
print ""

if players == "yes":
	p1 = raw_input("Player 1, what is your name? ")
	print "Hello " + p1, "You are player 1!"
	time.sleep(1)
	print ""

	p2 = raw_input("Player 2, what is your name? ")
	print "Hello " + p2, "You are player 2! Time to play Hang-Man!"
	time.sleep(1)
	print ""

	print p1 + ", enter a word you would like player 2 to guess."
	time.sleep(1)
	word = raw_input()
	
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print ""

	print p2 + ", Enter a character to start guessing!"
	time.sleep (0.5)

	guesses = ""

	turns = 10 

	while turns > 0:
		failed = 0
		for character in word:
			if character in guesses:
				print character
				
			else:
				print "[*]"
				failed += 1
				
		if failed == 0:
			print "You Won"
			print "The word was, " + word
			break	
		print ''
		
		guess = raw_input("Guess a character: ")
		
		guesses += guess
		
		if guess not in word:
			turns -= 1
			print "Wrong"
			print "You have, " + str(turns), " more guesses"
			
			if turns == 0:
				print "You Lose"
				print "The word was, " + word
				
elif players == "no":
	print ""
	print "Hello User what is your name?"
	user = raw_input()
	time.sleep(1)
	print ""
	
	print "Hello " + user + " ,welcome to Hang-Man!"
	time.sleep(1)
	print ""
	
	print "Here is the word you have to guess, have fun!:"
	time.sleep(1)
	print ""
	
	wordList = ("bigger", "table", "computer", "mouse", "mother", "turkey", "pencil", "cat", "eat", "mice", "daddy", "mummy", "son", "sister", "dog", "cat", "Antidisestablishmentarianism", "time", "robot", "julian")
	randomNumber = random.randint(0, len(wordList) - 1)
	word = random.choice(wordList)
	guesses = ""
	turns = 10
	
	while turns > 0:
		failed = 0
		for character in word:
			if character in guesses:
				print character
				
			else:
				print "[*]"
				failed += 1
				
		if failed == 0:
			print "You Won the game, I guess you're smarter then me!"
			print "The word was, " + word
			break	
		print ''
		
		guess = raw_input("Guess a character: ")
		
		guesses += guess
		
		if guess not in word:
			turns -= 1
			print "Wrong answer"
			print "You have, " + str(turns), " more guesses"
			
			if turns == 0:
				print "You have lost!"
				print "The word was, " + word + ", So if I beat you it means you lost to a bit of code, you're not that bright are you."
	
	

	
















