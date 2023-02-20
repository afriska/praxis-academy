#tuple is collection data which is ordered and unchangeable

tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
print(type(tpl), type(lst))

print('item2' in tpl)

tpl2 = ('item5', 'item6')
tpl3 = tpl + tpl2
print(tpl3)

#-----------------------------------------------------------------------#
empty_tpl = ()

boys = ('al', 'el', 'dul')
girls = ('maya',) #tanpa , dianggap string
siblings = boys + girls
print(siblings)
print(len(siblings))
family_members = siblings + ('father', 'mother')
print(family_members)
print(family_members[2])

#-----------------------------------------------------------------------#
fruits = ('Banana', 'apple', 'watermelon')
vegetables = ('tomato',)
animals_products = ('meat', 'milk')

food_stuff_tp = fruits + vegetables + animals_products
print(food_stuff_tp, type(food_stuff_tp))
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt, type(food_stuff_lt))

print('First three items:', food_stuff_lt[:3])
print('Last three items:', food_stuff_lt[len(food_stuff_lt)-3:])
print('Is banana in tuple?', 'banana' in food_stuff_lt)