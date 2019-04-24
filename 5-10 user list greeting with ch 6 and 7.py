#User list extended
# Python Crash Course. Copyright © 2016 by Eric Matthes
# 5-10 with elements from ch 6 and 7
# adding dictionaries and input functionality.

greetings = {
    "Admin": "Good morning Dave",
    "Bob": 'How do you use a computer with no hands?',
    "Larry": 'Larrycomputer 3000 tracking crime',
    "Harley": 'No you cant go into moms room',
    "Fluff": 'Stop walking across the keyboard',
    "Jack": 'No you cannot reset the system clock 500 years in the past',
    "Adam": 'we have given you access. Dont ruin it for us.',
    "Kirk": 'Good morning Captian',
    "Opensesme": 'Debug mode activated',
    }

Username = "nobody";            #username is initilized so the while function does not imediately quit
while Username != "die":        #this is a while function from chapter 7. It encompases the rest of the script  
    if Username  == "die":      #and will run over and over again until the word "die" is entered  
        break;
    
    if not greetings:                           # checks wether there are any entries in the greetings dictionary
    	print('NO USERS! RE-RUN SYSTEM SETUP');  #if the greetings dictionary is empty it shows a message

    Username = input ("What is you username? (I wont quit unless you tell me to die):");

    for  User in greetings.keys():  #loops through the usernames in the greetings dictionary. .keys tells it to look at the first value
    
        if Username == "opensesme":     #debug function to show the whole user list
            print("\n" + User );

        if Username  == "die":
            print("verry well");
            break;

        if Username.title() == User:    #shows greeting if your username is on the list
            print (greetings[User]);
 
    if Username.title() not in greetings.keys() and Username.title() != "Die":        #filling a dictionary with user input ch 7
        greetings[Username.title()] = "Welcome " + Username.title();
        print ("Welcome new user");


   #     print ("No we dont want any girl scout cookies");
    

