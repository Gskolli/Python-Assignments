#Assignment on LISTS

# Write a Python program to create a list.

lst = [1,2,3,4]
print(lst)

# Write a Python program to add an element to a list.

kids_name = ['vivaan','kairav','kayal']
print(kids_name)
kids_name.append('avni')
print(kids_name)
kids_name.insert(2,'kiyansh')
print(kids_name)

# Write a Python program to remove an element from a list.

kids_name = ['vivaan','kairav','kayal','avni']
print(kids_name)
kids_name.remove('kairav')
print(kids_name)

# Write a Python program to sort a list.

kids_age = [8,4,2,7,9,1,3]
print(kids_age)
kids_age.sort()
print(kids_age)

# Write a Python program to reverse a list.
kids_age = [8,4,2,7,9,1,3]
print(kids_age)
kids_age.sort()
print(kids_age)
kids_age.reverse()
print(kids_age)
kids_age = list(reversed(kids_age))
print(kids_age)

# Write a function to find the maximum and minimum element in a list.

lst1 = [10,20,30,40,60,50,70]
print(lst1)
lst1 = max(lst1)
print(lst1)

lst2 = [10,20,30,40,60,50,70]
print(lst2)
lst2 = min(lst2)
print(lst2)

# Write a Python program to find the sum of all elements in a list.

lst3 = [40,10,50,60]
print(lst3)

lst3 = sum(lst3)
print(lst3)

# Write a Python program to find the average of all elements in a list.

lst4 = [10,20,40,80,30]
print(lst4)
lst4 = ((sum(lst4))/len(lst4))
print(lst4)

# Write a function to find the maximum and minimum values in a list.

lst5 = [1,2,3,4,5,6]
print(lst5)

lst5 = ('minimum value= ',min(lst5),'maximum value= ',max(lst5))
print(lst5)

# Write a function to reverse the order of a list.

lst6 = [2,3,4,5,6,7]
print(lst6)
lst6.reverse()
print(lst6)
lst6 = list(reversed(lst6))
print(lst6)

# Write a function to sort a list in ascending or descending order.

lst7 = [100,300,500,700,200]
print(lst7)
lst7.sort()
print(lst7)
lst7.sort(reverse=True)
print(lst7)

Write a function to remove duplicates from a list.
Using set command
lst8 = [2,5,6,2,2,3,5,6,7]
print(lst8)
lst8 = list(set(lst8))
print(lst8)

#using for loop

result = []
for i in lst8:
   if i not in result:
       result.append(i)
print(result)    

#using for list comprehensions

result = []
lst8 = [result.append(i) for i in lst8 if i not in result]
print(result)

# Write a function to find the index of a given element in a list.

kids_name = ['vivaan','kairav','kayal']

print(kids_name.index('kayal'))

#print("vivaan" in kids_name) #boolean form
    
        
