import random
name = input("Enter your name:")
bag = {"green":6, "red":4}

total_money = 1000
rounds = int(input("How many rounds would like to play? "))

round = 0
while round < rounds:
	bet_amount = int(input("How much do you want to bet? "))
	user_pick = input("Do you want to pick a marble now? type 'yes' or 'no'"  )
	if user_pick.lower() == 'yes':
		marble = random.choice(list(bag.keys()))
		bag[marble] = bag[marble] - 1
		if marble == "green":
			total_money += bet_amount
			print(f'You picked %s. Great pick! Your total amount is now %s' %(marble, total_money))
		else:
			total_money -= bet_amount
			print(f'You picked %s. Aweful pick! Your total amount is now %s' %(marble, total_money))
		
	else:
		break

	if total_money <= 500:
		print("Game over, you are broke!")
		break
	round += 1
print(f"{name} thanks for playing this game! Your total amount is {total_money}")