#case Insensitive
# page 238 in Python crash course chapter 5 page 77 in pdf
# ignoring case when checking for equality
# when you want to check a value irregardless of its capitalization you can 
# check the the capitalized version of the name, or lowercase, uppercase, or titlecase for that matter.

myname = 'andrew'
print('my name is ' + myname)
print('Did I forget to capatalize my name?')
print(myname.title() == 'Andrew')
print('Am i still the same person?')
myname= 'Andrew'
print(myname.title() == 'Andrew')

