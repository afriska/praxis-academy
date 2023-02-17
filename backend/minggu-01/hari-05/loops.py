#-----------------------------------------------------------------------#
# for i in range(11):
#     print(i, end=' ')
# else:
#     print('\n')

# for i in range(10,-1,-1):
#     print(i, end=' ')
# else:
#     print('\n')

#-----------------------------------------------------------------------#
# for y in range(7):
#     for x in range(y):
#         print('#', end='')
#     print('\n')

#-----------------------------------------------------------------------#
# for i in range(9):
#     for i in range(9):
#          print('#', end=' ')
#     print('\n')

#-----------------------------------------------------------------------#
# for num in range(11):
#     print('%d x %d = %d' %(num, num, (num * num)))

#-----------------------------------------------------------------------#
# skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for skill in skills:
#     print(skill)

#-----------------------------------------------------------------------#
# for i in range(100):
#     if (i+1) % 2 == 0:
#         print(i+1)

# for i in range(1,101,2):
#     print(i)

#-----------------------------------------------------------------------#
# total=0
# for i in range(101):
#     print(i, end=' ')
#     total +=i
# else:
#     print('\n')
#     print('The sum of all numbers is %d.' %total)

#-----------------------------------------------------------------------#
# sum_evens = 0
# sum_odds = 0
# for i in range(101):
#     if i % 2 == 0:
#         sum_evens +=i
#     else:
#         sum_odds +=i
# else:
#     print('The sum of all evens is %d. And the sum of all odds is %d.' %(sum_evens, sum_odds))

#-----------------------------------------------------------------------#
fruits = ['banana', 'orange', 'mango', 'lemon']
reverse_fruits =[]
for i in range (len(fruits)):
    reverse_fruits.insert(-i, fruits[i])

print(fruits)
print(reverse_fruits)