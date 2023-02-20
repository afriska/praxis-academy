import re

# txt = 'I love to teach python and javaScript'
# match = re.match('I love to teach', txt, re.I)
# print(match)
# span = match.span()
# print(span)
# start, end = span
# print(end)
# substring = txt[start:end]

# print(substring)

#---------------------------------------------------------------------#

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first', txt, re.I) 
start, end = match.span()
print(txt[start:end])

match = re.findall('language', txt, re.I)
print(match)

match_replaced = re.sub('[Pp]ython', 'Javascript', txt, re.I)
print(match_replaced)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))