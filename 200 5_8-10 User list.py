#user list
# Python Crash Course. Copyright © 2016 by Eric Matthes
# 5-8 - 5-10 try it yourself
# pg 93 (pdf)
# I am trying the extra try it yourself progect as shown in the book


users = ['Bob', 'Larry', 'Harley', 'Fluff', 'Jack', 'Adam', 'Kirk', 'Admin']
#users=[]  # used to test line 39. no user test. Try it Yourself 5-9

new_Users = ['Adam', 'James', 'Mudler', 'jack']			#5-10

for user in users:
	if user == "Admin":
		print ("Good morning Dave");

	elif user == "Bob":
		print ('How do you use a computer with no hands?');

	elif user == "Larry":
		print ('Larrycomputer 3000 tracking crime');

	elif user == "Harley":
		print ('No you cant go into moms room');

	elif user == "Fluff":
		print ('Stop walking across the keyboard');

	elif user == "Jack":
		print ('No you cannot reset the system clock 500 years in the past');

	elif user == "Adam":
		print ('we have given you access. Dont ruin it for us.');

	elif user == "Kirk":
		print ('Good morning Captian');

if not users:
	print('NO USERS! RE-RUN SYSTEM SETUP');      #Try it Yourself 5-9


for new_User in new_Users:			#Try it yourself 5-10
	if new_User.title in users:
		print ("pick another username. " + new_User + " is allready taken");
	else:
		print (new_User + " has been added");




	
