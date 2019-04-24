#todo
# ch7 moving items from one list to another

todo = ['watch tv','dishes', 'laundry', 'watch tv', 'disasemble transmission', 'watch tv', 'study python', 'watch tv','watch tv', 'work on car', 'order car parts','watch tv','ride bike','watch tv'];
done =[];

print("Here are the items on your todo list:\n")
for item in todo:
    print (item);

print ("\n\nRemoving tv watching from the list. you dont have time to watch that much tv.\n\n");
while 'watch tv' in todo:
    todo.remove('watch tv',);

print("Your todo list now contains:\n")
for item in todo:
    print (item);

print('\n');

while todo:
    todo_item=todo.pop();
    
    print("doing: " + todo_item);
    done.append(todo_item);

if not todo:
    print("\nYou have done all of the things\n");
