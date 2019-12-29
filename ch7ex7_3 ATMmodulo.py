#Imaganary ATM
# ch7 excercise 7.3 (ish)
# The modulo opperator, and accepting input from the user.
# modified with while loop to make program persistant (ch 7)

loop_restart = ("Y");

while loop_restart == ("Y"):

	monney = int(input("Welcome to the Imaganary ATM where the numbers are made up and nothing matters. How much money do you want to withdraw today?"));

	if monney %20 == 0 and monney < 200:
		print("Here is your Monney");
	else:
		print("You have to go inside to withdraw that ammount");

	loop_restart = input ("Transaction complete another transaction? Y or N:\n").upper();
