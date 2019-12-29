#who Set
# chapter 6 page 108 set
# uses a new dictionary of various favorite dr who doctors 
# to display the function of the set attribute

favorite_doctors = {
    'harles': 1,
    'bob': 5,
    'john': 2,
    'Andrew': 4,
    'joe': 10,
    'jim': 10,
    'george': 4,
    'aiden': 11,
    'jill': 12,
    'tom': 9,
    }

print ("Favorite doctors: \n")
    
for doctor in set (favorite_doctors.values()):
    print (doctor);

#set will show only the unique values. 
