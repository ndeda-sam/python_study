#append ->used to add items at the end of the list

my_list=["mike","jane","alex",1000,200,2000,True,False]

my_list.append('Donkey')
print(my_list)

# insert _>adds an item in a specified index
my_list.insert(1,'mary')
print(my_list)
# pop-> removes an item at aspecified index
my_list.pop(3)
print(my_list)

#task
lst=[10,20,30,['Jane','mary',[1000,2000,3000]],40,50,60]
# using methods
# add 70 at end of the list
lst.insert(7,70)
print(lst)

# add 1500 btw 1000 and 2000
lst[3][2].insert(1,1500)
print(lst)
# delete 2000
lst[3][2].pop(2)
print(lst)

# sort -> used to arrange  list items asc by default
lst1=[1,50,10,20,5,2]
lst1.sort(reverse=True)
print(lst1)
lst2=["mike","jane","alex"]
lst2.sort()
print(lst2)
#remove
lst2.remove('alex')
print(lst2)
#extend
lst2=["mike","jane","alex"]
lst1=[1,50,10,20,5,2]
lst3=lst2+lst1
lst2.extend(lst1)
print(lst3)
#count
print(lst2.count('mike'))
# copy
lst4=lst1.copy
print(lst4)
# clear
my_list.clear()
print(my_list)
# in membership
lst2=["mike","jane","alex"]
print('alex' in lst2)