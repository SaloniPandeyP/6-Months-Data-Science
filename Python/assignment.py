 #✍️✍️Assignment 1 ✍️✍️

# Q1 Write a python to declare variables of different data types such as: 
# a) Integer 
# b) Float 
# c) String
# d)Boolean

# >>>>>> ...... 😊 Code Integer 😊.......>>>>>>

a = 12
print("Integer:-",(a))
print("<<<<<Data type :",type(a))

#>>>>>>>.........😊Code Float😊.......>>>>>>>>

b = 2.3
print(" float :-",(b))
print("<<<<< Data type:-",type(b))

#>>>>>>........😊 Code String 😊........>>>>>

c = "hello Shlau"
print(" String :",(c))
print("<<<<<Data type :-",type(c))

#>>>>>>........😊 Code Boolean 😊........>>>>>

is_saloni = True
is_notsaloni = False
print("correct name:-",is_saloni)
print("Data type:-", type(is_saloni))
print("wrong name:-", is_notsaloni)
print("Data type:-",type(is_notsaloni))

#Q2 Create a string variable with your name and perform the following operations:
#a) Convert it to uppercase
#b) Convert it to lowercase
#c) Find the length of the string
#d) Replace one character with another

#>>>>>>........😊 Code  😊........>>>>>
# Convert it to uppercase  >>>>>>>
name = "saloni"
print("Uppercase:-",name.upper())

# Convert it to lowercase  >>>>>>>
color = "PINK"
print("Lowercase:-",name.lower())

# Find the length of the string  >>>>>>>
name1 ="Saloni Pandey"
print("length of string:-",len(name1))

# Replace one character with another  >>>>>>>
name2 = "sholu"
print("Replace character:-",name2.replace("o" ,"a"))

#Q3. Write a Python program to check whether a given word is a palindrome or not using string slicing

word = "wow"
print("plaindrome:-",word[::-1])

#Q4. Create a list of 10 numbers and perform the following operations:
#a) Add a new element
#b) Remove an element
#c) Sort the list
#d) Find the maximum and minimum value

#>>>>>>........😊 Code  😊........>>>>>
lst =[1,2,3,4,5,6,7,8,9,20]
# Add new element
lst.append(23)
print("Add new element:-",lst)
# Remove an element
lst.remove(3)
print("remove element:-",lst)
# sort list
lst.sort()
print("sort the list:",lst)
# Find the max and min of the list
print("maximum number:-",max(lst))
print("minimum number:-",min(lst))

# Q5. Write a Python program to count how many even and odd numbers are present in a list

#>>>>>>........😊 Code  😊........>>>>>
lst =[1,2,34,5,62,35,6,8,96,86,24,54,76,67]
even = 0
odd = 0

for i in lst:
    if i % 2 == 0:
        even +=1
        
    else:
        odd +=1
print("count even =", even)
print("count  odd =", odd)

# Q6.Create a tuple containing 5 subjects. Print:
#a) First element
#b) Last element
#c) Length of the tuple
#d) Check whether a subject exists in the tuple or not

#>>>>>>........😊 Code  😊........>>>>>
sub =("DSA","OS","PYTHON","JAVA","OOPS")
# First element
print("First subject:",sub[0])

# Last  element
print("Last element:",sub[-1])

# Length of the tuple
print("Length of the tuple:",len(sub))

# Check whether a subject exists in the tuple or not
print("math" in sub)
print("dsa" in sub)
print("DSA" in sub)

# Q7. Write a Python program to create a dictionary of student details containing:
# a) Name
# b) Age
# c) Course
# d) Marks
# Then print all keys and values separately

#>>>>>>........😊 Code  😊........>>>>>
dict = { "name":"saloni",
        "age":20,
        "course":"DSA",
        "Marks":80
        }
print("My dictionary:-",dict)

print("all keys is:-",dict.keys())
print("all values is:-",dict.values())

# Q8.Write a Python program to update and delete elements from a dictionary.

#>>>>>>........😊 Code  😊........>>>>>
dict = { "name":"saloni",
        "age":20,
        "course":"DSA",
        "Marks":80
        }
# update
dict["Marks"] =82
print(dict)
#delete element
del dict["course"]
print(dict)

# Q9.Create two sets and perform the following set operations:
# a) Union
# b)Intersection
# c) Difference
# d) Symmetric Difference

#>>>>>>........😊 Code  😊........>>>>>
a ={1,3,5,2,6,7,8}
b ={2,4,5,3,6}
#union
print(a|b)
# intersection
print(a&b)
#differnce
print(a-b)
#Symmetric Difference
print(a^b)

# Q10. Write a Python program to remove duplicate elements from a list using a set.

#>>>>>>........😊 Code  😊........>>>>>
lst =[1,3,4,2,6,7,9,3,4,2,8]

unique_lst = list(set(lst))

print(unique_lst)