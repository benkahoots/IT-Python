import time

print "Make sure you are playing with 2 people!"
time.sleep(1.5)
print ""

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
print ""
word = raw_input()
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "
print "                                                                                                                  "



print p2 + ", Start Guessing..."
time.sleep (0.5)

guesses = ''

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
			print "You Loose"
			print "The word was, " + word
