#made the users script from chapter 7 into a function to practice 
#to practice function info from chapter 8.

#users Again
#ch7 filling a dictionary with user input pg 130 (windows)
# when presented with a new username the script adds the user to the list.
# the user list and dictionary is probably redundnat but whatever.
# compiled all the person names I have used in my scripts


def users7(username):
    

    users = ["Admin","Bob","Larry","Harley","Fluff","Jack","Adam","Kirk","Opensesme",'bob','jimmy','jerry','lisa','linda','casey','colby', 'zendarr', 'Bloaty', 'harles','bob','john','Andrew','joe','jim','george','aiden','jill','tom']


    
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

    username = username.title();
    print ("Hello " + username);
        
    if username not in users:
        messsage = input("\nwhat message would you like to be greeted with when you log in?")
        greetings[username] = messsage;
        users.insert(0,username);
    else:
        if username in greetings:
            print (greetings[username]);
        else:
            print("you allready have a user");
        
on = True;

while on:
    username = input ("what is your username?");
    if username.title() == ("Quit"):
        on = False;
        continue
        
    users7(username);

