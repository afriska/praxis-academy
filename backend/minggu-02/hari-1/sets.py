#set is collection items unordered and un-indexed elements
st = {'item1', 'item2', 'item3', 'item4'}
print(type(st))
print(len(st))
print(st)
st.add('item5')
print(st)
st.remove('item3')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st1.intersection(st2))
print(st2.issubset(st1))
print(st1.issubset(st2))
print(st1.difference(st2))
print(st2.symmetric_difference(st1))

#-----------------------------------------------------------------------#