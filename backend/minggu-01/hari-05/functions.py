# def generate_full_name():
#     first_name = 'afriska'
#     last_name = 'yusuf'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)

# generate_full_name()

# def add_two_numbers():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total

# result = add_two_numbers()
# print(result)

# def area_of_circle(r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area

# print(area_of_circle(10))

# def weight_of_object (mass, gravity):
#     weight = str(mass * gravity) + 'N.'
#     return weight

# print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

#----------------------------------------------------------------------#
# def add_two_numbers(a, b):
#     return a + b

# print(add_two_numbers(12,28))

#----------------------------------------------------------------------#
# def convert_celcius_to_fahrenheit(c):
#     return  (c * 9 / 5) + 32

# print(convert_celcius_to_fahrenheit(5))
#----------------------------------------------------------------------#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# def print_list(lst):
#     for item in lst:
#         print(item)

# print_list(fruits)

#----------------------------------------------------------------------#
def evens_and_odds(num):
    numOdds = 0
    numEvens = 0
    for i in range(num + 1):
        if i % 2 == 0:
            numEvens += 1
        else:
            numOdds +=1
    else:
        print('The number of odds are %d.' %numOdds)
        print('The number of evens are %d.' %numEvens)

print(evens_and_odds(100))

#----------------------------------------------------------------------#