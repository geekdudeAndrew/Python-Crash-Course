#updated Ommlettte
# Updated "pg53-63 ch4 Lists ommelette" with a while loop and user input
# pretends to be a commandline game where you feed your neopet.
# it has a funny ending.
 

food = ['plain ommelette','pepperoni ommelette', 'green pepper ommelette',
 'pepperoni and sausage ommelette', 'orange jelly', 'lime jelly', 
 'mint jelly', 'breadfish']

print ("\nYou have just spent hours playing dumb games on an internet site where you");
print ("pretend to have a strange pet like its 1999 or something. your pockets are full");
print ("of some wet food items that do not belong there. your pet Firelizard is hungry \n")

while food:
	print ("This is what you have in your pockets: ")
	print (*food, sep = ', ');
	print ("\n");

	eat = input ("Which food item do you want to feed to Sparky? ");
	
	if eat in food:
		print (eat + " mmm thats some good eatin. \nYour firelizard eyes you hungrly \n");
		food.remove(eat);
	else:
		print: ("That doesnt make since \n"); 


print ("your pet Firelizard George, having just watched you stuff yourself, dies of ");
print ("hunger. I guess you should have fed George sometime in the last 10 years sparky.\n")

"""
for food_item in food:
	print ("just ate a " + food_item.title() + " mmm thats some good eatin ")
	print ("yep nothin like a tasty " + food_item.title() + 
	" I realy like " + food_item.title() +"s .\n")
# plural nouns not propperly executed
"""

