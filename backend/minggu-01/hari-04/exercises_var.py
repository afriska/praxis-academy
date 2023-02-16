#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md

a, b, first_name, last_name = 28, 12, 'afriska', 'yusuf'
print(a)
print(b)
print(first_name)
print(a, b, first_name, last_name)
print('len of name:', len(first_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))

num_one = 4
num_two = 2
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius * radius
circum_of_circle = 2 * 3.14 * radius

r_str = input('Input radius: ')
r = int(r_str)
area = 3.14 * r * r
print(area)

first_name = input('Input your first name : ')
last_name = input('Input your last name : ')
country = input('Input your country : ')
age = input('Input your age : ')

print(first_name, last_name, country, age)
print(type(age))
