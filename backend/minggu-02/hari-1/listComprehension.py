language = 'Python'
lst = list(language)
lstcom = [i for i in language]
print(lst)
print(lstcom)

numbers = [-8, -7, -3, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positiveNums = [i for i in numbers if i >= 0]
print(positiveNums)

#-----------------------------------------------------------------------#

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negzero = [i for i in numbers if i < 1]
print(negzero)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

lst_of_tpl = [tuple([j ** i for i in range(6)]) for j in range(11)]
print(lst_of_tpl)

#-----------------------------------------------------------------------#