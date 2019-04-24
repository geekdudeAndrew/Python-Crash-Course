#try it yourself 5-11 pg 93 ordinal numbers
# add ending to numbers 1-9
# make a program to list numbers 1-9 and add the ending th,st,or rd
# as appropriate. extended to be able to count as high as needed.

print ("\nOrdinal Numbers ")
print("pg 93 Try it yourself 5-11  \n")


for value in range (1,36):
    if value == 11:
        print (str(value) + 'th')
    elif value == 12:
        print (str(value) + 'th')
    elif value == 13:
        print (str(value) + 'th')
    
    elif str(value)[-1] == '1':
        print (str(value) + 'st');
    elif str(value)[-1] == '2':
        print (str(value) + 'nd');
    elif str(value)[-1] == '3':
        print (str(value) + 'rd');
    else:
        print (str(value) + 'th');
