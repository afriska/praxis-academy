# # greeting = 'Hello, World!'
# # print(greeting)
# # print(len(greeting))
# # multiline_string = '''I am a teacher and enjoy teaching.
# # I don't find anything as rewarding as empowering people.
# # That is why I created 30 days of python.'''
# # print(multiline_string)

# # #gabungin string
# # first_name = 'afriska'
# # last_name = 'yusuf'
# # space = ' '
# # full_name = first_name + space + last_name
# # print(full_name)

# # # \n: new line
# # # \t: Tab means(8 spaces)
# # # \\: Back slash
# # # \': Single quote (')
# # # \": Double quote (")
# # #%s for string
# # #%d for integers
# # #%f for floating

# # formated_string = 'I am %s %s' %(first_name, last_name)
# # print(formated_string)

# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # print('The area of circle with a radius %d is %f' %(radius, area))
# # print('The area of circle with a radius %d is %.2f with 2 significant digits after the point' %(radius, area))

# # #unpacking characters
# # #string kumpuluan karakter dipisah menjadi per karakter

# # language = 'Python'
# # a,b,c,d,e,f = language
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(e)
# # print(f)
# # first_letter = language[0]
# # second_letter = language[1]
# # last_index = len(language)-1
# # last_letter = language[last_index]
# # print(first_letter)
# # print(second_letter)
# # print(last_letter)
# # second_last = language[-2]
# # print(second_last)

# # name = 'afriska'
# # last_three = name[-3:]
# # four_last = name[3:]
# # print(last_three)
# # print(four_last)

# # reverse_name = name[::-1]
# # print(reverse_name)

# # fik = name[1:7:2] #[start:stop:interval]
# # print(fik)

# #capitalize() first character of string to capital
# challenge = 'thirty days of python'
# print(challenge.capitalize())

# #count() counting in char in string
# print(challenge.count('y', 3, 14)) #(substring, start, end)

# #endswith() check ending
# print(challenge.endswith('on'))
# print(challenge.endswith('tion'))

#expandtabs() tab to spaces, default size is 8
tes = 'thirty\tdays\tof\tpython'
print(tes)
print(tes.expandtabs())
print(tes.expandtabs(10))
print(tes.expandtabs(10))

# #find() return first index founded, if not found return -1
# challenge = 'thirty days of python'
# print(challenge.find('y')) 
# print(challenge.find('ti')) 

# #rfind() like find() but last
# print(challenge.rfind('y')) 
# print(challenge.rfind('th'))

# #index() return lowest index of substring, not found error
# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 0, 9)) # error

# #rindex() like index() but highest index
# #isalnum() checks alphanumeric char, space not a alnum
# test = '30days'
# print(test.isalnum())
# test = '30 days'
# print(test.isalnum())

# #isalpha() checks just alpha char
# test = ' days'
# print(test.isalpha())

# #isdecimal() checks if decimal
# #isdecimal() checks if all numbers and some other unicode char for numbers


