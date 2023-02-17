# #list ordered changable allows duplicate
# lst = list()
# empty_list = list()
# print(len(empty_list))
# lst = []

# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']
# web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Countries:', countries)
# print('Number of countries:', len(countries))

# first_fruit = fruits[0]
# print(first_fruit)
# first_fruit = fruits[-4]
# print(first_fruit)   

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))
tem = list(enumerate(s1,1))
print(type(tem))
print(tem)
print(tem[1])

