print("Using If statements with lists")
print("using multiple lists") 
print("pg92 ch5 \n")

approved_foods = ["granola", "suet cake", "pills", "veggie chilli", "cornbread"];

requested_foods = ["icecream", "candy", "soda", "bread", "pizza", "Rolls", "hamburgers", "steak", "pancakes", "veggie chilli"];

for requested_food in requested_foods:
    if requested_food in approved_foods:
        print("you can have " + requested_food);
    else:
        print(requested_food + " is not on your vegan anti gluten diet.");
