# Rock Paper Scissors Game 

# Goal:
# - Ask the player if they pick rock paper or scissors
# - Have the computer chose its move
# - Compare the choices and decide who wins
# - Print the results

# Subgoals:
# - Let the player play again
# - Keep a record of the score e.g. (Player: 3 / Computer: 6)


from random import randint

def answerToNum(answer):
	if answer == 'rock':
		return 0
	elif answer == 'paper':
		return 1
	elif answer == 'scissors':
		return 2
	else:
		return "error"

def numsToText(num1,num2):
	if num1 == 0 and num2 == 2:
		return "\nRock beats scissors!"
	elif num1 == 1 and num2 == 0:
		return "\nPaper beats Rock!"
	elif num1 == 2 and num2 == 1:
		return "\nScissors beats paper!"

keepPlaying = True
score = [0,0,0]

# intro to game
print ("\nWelcome to Rock, Paper, Scissors!")
print ("----------------------------------")

# beginning of loop
while keepPlaying:
	# prompt for user input and logic for random computer answer
	player = raw_input("\nPlease Pick:\n-Rock\n-Paper\n-Scissors\n\nAnswer: ").lower()
	player = answerToNum(player)
	#print player
	if player not in [0,1,2]:
		print "\nError invalid response. Starting over...\n----------------------------------------"
		continue

	# get computer choice
	computer = randint(0,2)

	#LOGIC
	if (int(player)==computer): 
		print("\nIt's a tie!")
		score[2] += 1
		print ("--------------------------\nSCORE [player, computer, tie]: ")
		print score
	elif((int(player)-computer) % 3 == 1):
		print numsToText(player,computer)
		print ("You win!")
		score[0] += 1
		print ("--------------------------\nSCORE [player, computer, tie]: ")
		print score
	else:
		print numsToText(computer,player)
		print("The computer beat you!")
		score[1] += 1
		print ("--------------------------\nSCORE [player, computer, tie]: ")
		print score


	# ask if user wants to play again 
	# if no figure who won and print score
	play_again = raw_input("\n--------------------------\nPlay Again? (yes/no): ").lower()
	if play_again == "no":
		keepPlaying = False
		print "\n\n*************************************"
		
		if score[0] > score[1]:
			print "You win! Congratulations!"
		elif score[1] > score[0]:
			print "You lost... The computer beat you."
		else:
			print "How did you manage to tie that much? Oh well."

		print ("FINAL SCORE [player, computer, tie]: ")
		print score
		print "*************************************\n"
	elif play_again =="yes":
		continue
	else:
		print "\nError, I don't understand so I'll assume that's a no...\n"
		break
		
# V2: complex logic






