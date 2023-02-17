#======================================================================#
# age = int(input('Enter your age: '))

# if age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print('You need %d more years to learn to drive.' %(18 - age))

#======================================================================#
# num1 = int(input('Enter number one: '))
# num2 = int(input('Enter number two: '))

# if num1 > num2:
#     print('%d is greather than %d' %(num1,num2))
# elif num1 < num2:
#     print('%d is smaller than %d' %(num1,num2))
# else:
#     print('%d equal to %d' %(num1,num2))

#======================================================================#
# month = input('Enter this month: ')
# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

# if month in autumn:
#     print('The season is Autumn')
# elif month in winter:
#     print('The season is Winter')
# elif month in spring:
#     print('The season is Spring')
# else:
#     print('The season is summer')

#======================================================================#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Enter the fruit you want to check: ')
# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)

#======================================================================#
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML', 'CSS'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if len(person['skills']) > 0:
    if len(person['skills']) %2 != 0:
        mid = len(person['skills']) //2
    else:
        mid = (len(person['skills']) //2)-1    
    print(person['skills'][mid])

print(person['skills']) if 'Python' in person['skills'] else print('No Python skill')

if person['is_married'] and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], 'lives in', person['country']+ '. He is married')

#======================================================================#