#dictionary Pizza
# pg 110 ch 6 range of dictionaries
# automatically adding nested dictionaries to a list


print("bloaty wants more pizzas lets make some \n")

Pizzas = []

for pizza_number in range(50):
    new_pizza = {'topping': 'pepperoni', 'crust': 'deep dish', 'size': '20 inch'}
    Pizzas.append(new_pizza)
    
for pizza in Pizzas[0:7]:
    if pizza['topping'] == 'pepperoni':
        pizza ['topping'] = 'sausage'
        pizza ['crust'] = 'thin crust'
        pizza ['size'] = 'personal pan'
    

for pizza in Pizzas[:12]:
    print(pizza)
print ('also more ...\n')

print(str(len(Pizzas)) + ' Pizzas total \n I eat too many pizza')
