import os
import random

def rpsLogic(nc,sc):
	# if statements return two numbers corresponding to 
	# correct dictionary values represented by 'result' and 'reason'
	if nc == sc: return 0, 0 				#"It's a tie!"
	elif nc == 0 and sc == 1: return 2, 2	# Saint wins! Paper beats Rock."
	elif nc == 0 and sc == 2: return 1, 1 	# North wins! Rock beats Scissors"
	elif nc == 1 and sc == 0: return 1, 1	# North wins! Paper beats Rock."
	elif nc == 1 and sc == 2: return 2, 2 	# Saint wins! Scissors beats Paper."
	elif nc == 2 and sc == 0: return 2, 2 	# Saint wins! Rock beats Scissors."
	elif nc == 2 and sc == 1: return 1, 1 	# North wins! Scissors beats Paper."

def stop(userInput):
	return False if userInput == 'n' else True # breaks loop to quit

def clrScreen():
	osname = os.name
	if osname == 'posix': os.system('clear')
	elif name == 'nt' or name == 'dos': os.system('cls')
	else: print("\n" * 30)

nw, sw, t, games, repeat = 0, 0, 0, 0, True
RPS = { 
	0: "Rock", 
	1: "Paper", 
	2: "Scissors" 
	}
reasonWords = { 
	0: "It's a tie!"
	1: "Paper beats Rock.",
	2: "Rock beats Scissors.",
	3: "Scissors beats Paper.",
	}
resultWords = {
	0: "Nobody wins!" 
	1: "North wins!",
	2: "Saint wins!",
	}

while games < 100:	
	games = games + 1 # increment games played
	
	# clears screen 
	clrScreen()

	print "\nPaper Scissors. North West vs. Saint West:"
	print "----------------------------------------------"	
	
	# USE THIS TO IMPLEMENT SUDO AI FOR COMPUTER PICKING
	northsChoice, saintsChoice = random.randint(0,2), random.randint(0,2)	
	
	# Print throws, and run loop logic for RPS
	print "North throws {}! Saint throws {}!".format(RPS[northsChoice], RPS[saintsChoice])
	result, reason = rpsLogic(northsChoice,saintsChoice) # result: 0=north, 1=saint, 2=tie
	print ("{} {}\n").format( outcomeWords[result], outcomeWords[reason] )

	# tally and print results / games played
	if result == 4: nw = nw + 1 
	elif result == 5: sw = sw + 1
	elif result == 6: t = t + 1
	print ("Score: North: {} South: {} Ties: {}\nGames: {}").format(nw,sw,t,games)
	
print os.name
	# continue with game
	# repeat = stop(raw_input("Would you like to quit (y/n): "))


	

# NEW GOALS
# ----------------------
# COM v COM
# P1 v COM
# P1 v P2
# COM weighter AI
# make things objects



# Rock Paper Scissors Challenge
# -----------------------------------------
# say what's gonna happen
# generate two random numbers for two users
# compare numbers
# pick winner 
# print who won

# BONUS:
# tally who won
# print tally
# repeat
# else: print "you forgot one {} and {}".format(nc,sc) 


# choice1,choice2 = random_number(),random_number() 