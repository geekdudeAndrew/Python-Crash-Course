#Ommlette Lists
# ch4 pg 53-63 up to Simple Statistics with a List of Numbers
# Displays list making by applying the concept to a diffrent
# situation. 

food = ['plain ommelette','pepperoni ommelette', 'green pepper ommelette',
 'pepperoni and sausage ommelette', 'orange jelly', 'lime jelly', 
 'mint jelly', 'breadfish']
for food_item in food:
	print ("just ate a " + food_item.title() + " mmm thats some good eatin ")
	print ("yep nothin like a tasty " + food_item.title() + 
	" I realy like " + food_item.title() +"s .\n")
# plural nouns not propperly executed

print ('I eat too many pizza ')
print ('\nhow many pizzas did i eat?')

#for value in range (1,21):
#	print (value)

#numbers= list(range(2,21,2))	#Third number shows how many to skip
#print (numbers)

#numbers=[]
#for value in range(1,21):
#	numbers.append(value**2)		# ** is the sign for exponent


numbers=[value**2 for value in range(1,21)]
print(numbers)
#replaces imediately above function with a list comprehension.



print('I eat '+ str(sum(numbers)) + ' pizzas \n')




million=[value**2 for value in range(1,1000000)]
print(max(million))
print(sum(million))
