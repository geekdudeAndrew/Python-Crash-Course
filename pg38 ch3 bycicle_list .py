#Bicycle List
# chapter 3 list operations
# page 38 in pdf

# I think the terminal colors (\033[1m) only work on unix based systems. They wont work correctly on windows

#list
print("\nFinding bicycles")
original_bicycles = ['giant', 'trek', 'cannondale', 'red-line', 'specalized', 'surly', 'mongoose', 'genesis', 'schwinn'];
print('copying bycicles to another list before messing with the list')
bicycles = (original_bicycles[:])		#to copy a list you have to point it to a slice. if you point it to the list then the new variable just becomes a pointer and not a new list. 
print("Changing red-line to red line")
bicycles[3] = 'red line'           # changed bicycle 3 to "red line from red-line removed the dash"
print("Adding roadmaster at the 6th position")
bicycles.insert(6, 'roadmaster');	# added roadmaster at position 6
print('Deleting bicycle #7 mongoose')
del bicycles [7];					# deleted bike 7 mongoose

print('Adding chumba to the end of the list')
bicycles.append('chumba')				#added chumba to the end of the list
print('Adding wright brothers to the beginning of the list')
bicycles.insert(0, 'wright brothers')	#added wright brothers to the begining of the list. they were a bicycle manufacturer before they made their flight.
print('Deleting wright brothers')
del bicycles[0]							#deleted item # 0 wright brothers that I just added. 
print('Removing red line')
bicycles.remove('red line')				#removed red line
print ('Sorting list in reverse order')
bicycles.reverse()						#sort list in reverse

print('\nPrinting each bicycle on a new line with a loop \n')
for index in range(0,len(bicycles)):	#Loop to print all items in bicycles
	print(bicycles[index].title());		

popped_bicycle = bicycles.pop()			#remove the last item on the list and put it in a variable
#bicycles.sort(reverse=True)
print('\n\033[1m printing bicycles in reverse order which is actually forward order.\n\033[0m')		
print(sorted(bicycles, reverse=True))	#print bicycles in reverse order which is actually now forward order.

print ("\033[1m\nRemoving these from the list with pop funciton:\033[0m")

print (bicycles.pop())					#show the value of the item that we removed earlier
print (popped_bicycle)					#delete the last variable and show its value

print ('There are '+ str(len(bicycles)) +' bicycles left')

print ("\n"+'\033[1m'+"Bicycles 1-4 in the list are as follows\n\033[0m" + str(bicycles[1:5]) + "\nthis is known as a list slice")
print ('\033[1mBicycles 0-1:\033[0m ') # \033[1m is an escape character a holdover from the days of physical terminals. /033 is just a way of indicating the escape key and the 1m indicates bold 0m returns to normal
print (bicycles[:2])		#if the first number is not there it just starts at 0
print ('\033[1mBicycles from number 5 to the end of the list:\033[0m ')
print (bicycles[5:])			#similar functionality with the second number
print ('\033[1mand the last 3:\033[0m ')
print (bicycles [-3:])		#-3 indicates the third from the last element. we are showing all elements from there onward
print('\033[1meverything up to the third from the last element:\033[0m ')
print (bicycles[:-3])

print ('\033[1m\nprinting the last 4 bicycles using a for loop: \033[0m' )

for bike in bicycles [-4:]:
	print (bike.title())
print ('\033[1m\noriginal list of bicycles:\033[0m')	
print (original_bicycles)
