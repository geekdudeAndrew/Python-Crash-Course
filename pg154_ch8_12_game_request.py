"""
Game design query
Chapter 8-12 page 154 (pdf)
Declared a function that can accept an arbitrary ammount of Arguments
automated responce for game design requests to a game design company
"""

def gamerequest (Title, dimensions, perspective, game_type, email, *details):
    print ('Your game request is as follows:\n\n' +
    'Title: ' + Title + ' \n' +
    dimensions + ' ' + perspective +  ' ' + game_type + ' \n'
    );
    
    for detail in details:
        print(detail + ' ');
    
    
    
    print ('\nYour Request has been recieved  and catalogued. If we find \n' +
    'your progect intresting we may call you. however we are a small \n' + 
    'gamedev company and we are hard at work on our own amazing ideas.\n' +
    'We would encourage you to try your hand at learning gamedev yourself.');

gamerequest ('Chrisses Castle', '2d', 'Top down', 'Puzzle/adventure','me@me.com', 
'fun', 'challanging', 'diffrent', 'touching', 'genere defying')
