#if Apples
# pg77 ch5 Checking for Inequality
# displaying use of an if statement to display a list 
# and using the inequality operator in order to conditionaly change case of list elements.

apples = ['granny smith', 'red delicious', 'golden delicious', 'fuji', 
'jonathan', 'jonagold', 'koru', 'pink lady', 'honneycrisp', 'imac', 'Mac Classic', 
'macbook pro', 'emac', 'preforma', 'g3', 'g4','g5', 'apple IIgs', 'lisa']

for apple in apples:
 #   if apple.lower() == 'imac':      #every time it finds the word imac or emac
 #       print(apple.lower())         #it will print it in lowercase
#    else:
#        if apple.lower() == 'emac':    #I understand the second letter is susposed
#            print(apple.lower())       #to be capatilized but idk how to do that yet
#        else:                          #rewrote this part to make it simpler
#            print(apple.title())       

    if apple.lower() != 'imac':
        if apple.lower() != 'emac':
            print (apple.title())
    else:
        print(apple.lower())
