from gameComponents import gameVars

def comparing():
	if gameVars.computer_choice == gameVars.player_choice:
		print("Draw!!====><====")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			gameVars.player_lives -= 1
		else:
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			gameVars.computer_lives -= 1
		else:
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			gameVars.player_lives -= 1

	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			gameVars.player_lives -= 1
		else:
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			gameVars.computer_lives -= 1