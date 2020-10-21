print('This is a recipe scaler for serving large crowds')
print('When using this program make sure to denote spaces in the name of your ingredients with a _ or a -!')
print('Enter one ingredient per line, with a numeric value first')
#This while loop will take the input of the recipe and print out what the recipe is. It will also break the input into Three parts of the code and will then be able to record those inputs into a dictionary
x = 0
recipe_dict = {
    }
a = 1
b = 1
counter = 1
while x == 0:
    z = input('')
    if len(z) > 0:
        y = len(z)
        recipe_dict.update({a:z})
        a += 1
        counter += 1
    else:
        x +=1
        
print('Here is the recipe that has been recorded')
a = 1
while b != 0:
    if a != counter:
        z = recipe_dict[a]
        quant, unit, item = z.split(' ')
        print(repr(quant).rjust(2), repr(unit).rjust(3), repr(item).rjust(4),end=' ')
        a += 1
    else:
        b -= 1
import math
people_served = int(input('How many does this recipe serve? ', ))
people_coming = int(input('How many people must be served? ', ))
scaleby = people_coming / people_served
scaleby = math.ceil(scaleby)
print('Multiplying the recipe by', scaleby)
print()

a = 1
c = 1
while c != 0:
    if a != counter:
        z = recipe_dict[a]
        quant, unit, item = z.split(' ')
        if '/' in quant:
            numer, slash, denom = quant.partition('/')
            quant1 = int(numer)
            quant2 = int(denom)
            print(quant1 * scaleby,'/', quant2 * scaleby, '%5s' % unit, '%5s' % item, sep ='')
        else:
            quant1 = int(quant)
            print(quant1 * scaleby,'%5s' % unit, '%5s' % item,)
        a += 1 
    else:
        c -= 1
