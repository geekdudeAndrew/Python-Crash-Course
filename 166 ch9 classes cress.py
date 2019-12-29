# ch9 classes 9-1,9-3 pg 161-166
#using my game Cresses Castle as a personaly relevant topic to practice


class Character():
    """a simple example of classes using the theme of my game cresses castle"""
    
    def __init__(self, name, color, bio):                               #The __init__() Method pg163(PDF)
        """Initilize attributes"""
        self.name = name;
        self.color = color;
        self.bio = bio;
        self.direction = "south";                                       #Setting a default value for an attribute pg168 (pdf)
    
    def walk (self, direction):
        """simulate a character walking. changes the direction of the charicter and prints a walk message"""
        
        if (direction == "north" or direction == "south"           #Modifying an Attribute’s Value Through a Method
            or direction ==  "west" or direction ==  "east"):           #pg 169-170 (pdf)
                self.direction = direction;
                print(self.name.title()+ " cautiously walks through the castle" + 
                " in the the "+ self.direction + "ward direction ");
        else:
            print(direction + " is not an actual direction");
            
    def look(self):
        print(self.name.title() + " is wearing " + self.color + " clothes and is facing " + self.direction);
    
    def start_menu(self):
        """simulate a pause menu"""
        print("\n________________________________________________");
        print("|"+ self.bio +"|");
        print("------------------------------------------------\n");
      
cress = Character("Cress", "Yellow",                                    #Making an Instance from a Class pg164(pdf)
    ("Normal factory worker. Finds rift in spacetime"));
cress.walk('east');                                                     #Calling Methods
cress.walk('north');                                                    #pg 165 (pdf)
cress.walk('south');
cress.walk('west');
cress.walk('west');
cress.direction='south';                                                #Modifying an Attribute’s Value Directly pg 169 (pdf)
cress.start_menu();


Grandma = Character ("Grandma", "Purple",                               #Creating Multiple Instances pg 165-166(pdf)
    "Lonely old lady accidentaly trapped by spacetime rift inside precarious broken down area of castle. Blind");
Grandma.walk ("dennis");
Grandma.walk ("west");
Grandma.start_menu();

Grandma.look();
cress.look();



class Ice(Character):
    """Represents Snow Princess charicter in another class"""
    
    def __init__ (self, name, color, bio):
        super().__init__(name, color, bio);                             #The __init__() Method for a Child Class pg 172-173 (pdf)
    
    def Iceblast(self):                                                  #Defining Attributes and Methods for the Child Class pg 174(pdf)
        print(self.name + " shoots a blustery blast of snow and ice to the " + self.direction);
    
snowprincess = Ice("Snow Princess", "Light blue", "leader of the ice kingdom. Able to use the royal ice magics");

snowprincess.start_menu();

snowprincess.look();

snowprincess.walk("north");
snowprincess.Iceblast();

