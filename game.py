from random import randint

from gameComponents import gameVars, winOrLose, comparing


while gameVars.player_choice is False:
	print("!!==================!!!!! (Σ( ° △ °|||)You meet a Monster !!!!!==================!!")
	print("(-`д´-)You are a Monster Hunter!! Please kill the Monster!!")
	print("The Monster HP:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Monster Hunter HP:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===================================================================================")
	print("Choose your weapon to kill the Monster!!! Or type quit to exit\n")

	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

	if gameVars.player_choice == "quit":
		print("You chose to quit")
		exit()

	print("The Monster Hunter chose: " + gameVars.player_choice)

	gameVars.computer_choice = gameVars.choices [randint(0, 2)]

	print("The Monster chose: " + gameVars.computer_choice)

	comparing.comparing()

	if gameVars.player_lives == 0:
		winOrLose.winorlose("are dead by the monster(×_×;）")

	if gameVars.computer_lives == 0:
		winOrLose.winorlose("killed the Monster!!! You save the world!!!٩(●˙▿˙●)۶…⋆ฺ")
		
	print("Monster Hunter HP:", gameVars.player_lives)
	print("The Monster HP:", gameVars.computer_lives)

	gameVars.player_choice = False

