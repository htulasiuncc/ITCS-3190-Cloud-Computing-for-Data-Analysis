#!/usr/bin/env python
# coding: utf-8

# # Part 1: Declaring Variables and Printing

# #### You may be familiar with the conventional way of initializing variables, shown below:

# In[69]:


x = "ITCS 3190"


# In[70]:


print(x)


# #### Python, however, offers another way of initializing variables, in which you can do it in one line. To do this, delimit the variable names and the variable values as shown below

# In[73]:


a,b = "Python", 3


# In[74]:


print(a)


# In[75]:


print(b)


# #### Now try and initialize three variables, "FirstName", "LastName", and "StudentIDNumber" using a similar method. Make sure to use your name and student ID number for this part.

# In[76]:


FirstName, LastName, StudentIDNumber = "Hima", "Tulasi", 800724155


# #### Now, let's try and print it all on one line, saying "My name is (FirstName) (LastName), and my Student ID number is (StudentIDNumber)." using Python's simple "print" statement. One thing to note is that Python does not support concatenating strings and ints, so you may have to figure out how to cast age to a string value to get this to work successfully.

# In[77]:


print("My name is " + FirstName + " " + LastName + ", and my Student ID number is " + str(StudentIDNumber) + ".")


# # Part 2: Importing Libraries

# #### We will be using a variety of libraries this semester, including numpy, pandas, and sklearn, so it is necessary to know how to import modules, and can be done as seen below.

# In[78]:


import pandas
import numpy as np
from random import randint
import statistics as stats


# #### Now, import the "statistics" module as "stats" and use the median method to find the median of the list below in the empty cell

# In[79]:


numList = [24,84,28,55,58,82,98,12,14,8,64,30,78]


# In[80]:


stats.median(numList)


# # Part 3: Lists

# #### First let's explore how to declare a list, and then the operations we can do upon a list

# In[81]:


fruits = ["apple", "banana", "pineapple", "mango", "watermelon"]


# #### We can find the length of the list

# In[82]:


len(fruits)


# #### We can index the items in a list, and even index a particular item

# In[83]:


fruits[2]


# In[84]:


fruits[2][5]


# #### We can also slice lists, and we do so using the format below

# In[85]:


fruits[2:]


# In[86]:


fruits[:3]


# In[87]:


fruits[2:4]


# In[88]:


fruits[::2]


# #### The general format for the slicing is [start:stop:step], with step being 1 by default. The start is inclusive, and the stop is exclusive, meaning if you go from index 1 to index 4, it will include index 1 up through the index immediately before index 4, which would be index 3. The step value tells us how big steps should be from one item to the next in the slice. Whether we should include every item, every other item, every 3rd item, etc.

# #### You can also add items to the end of the list

# In[89]:


fruits.append('peach')
fruits


# #### You can add items in at a specific index

# In[90]:


fruits.insert(1, 'plum')
fruits


# #### You can delete items at specific index

# In[91]:


del fruits[1]
fruits


# In[ ]:





# #### You can delete items by name as well

# In[92]:


fruits.remove('peach')
fruits


# #### Now, take the below list named alphabet, and use the above operations to follow the instructions in each step. Make sure to write the list name on a new line after the operation to print the list in Jupyter and ensure you are doing the right thing as I have done above with the fruits list.

# In[119]:


alphabet = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']


# #### Use a function to find the length of the list and make sure it is the correct length

# In[120]:


len(alphabet)


# #### If the list is not the correct length, use the add operations above to correct the alphabet

# In[121]:


alphabet.insert(6, 'g')


# In[122]:


alphabet.insert(26, 'z')


# #### Print every other item in the list from item 2 to item 15

# In[123]:


alphabet[1:14:2]


# #### Remove the first three alphabetically occuring vowels by their indices

# In[124]:


del alphabet[8]


# In[125]:


del alphabet[4]


# In[126]:


del alphabet[0]


# #### Remove the remaining vowels by their value

# In[127]:


alphabet.remove('o')


# In[128]:


alphabet.remove('u')


# In[129]:


alphabet.remove('y')


# #### Print the final list

# In[130]:


print(alphabet)


# #### You can also add lists together and make a new list using +. Use the + to make a new list called fruitAlphabet.

# In[131]:


fruitAlphabet = fruits + alphabet


# # Part 4: Tuples

# #### If you recall, tuples are immutable, so there are limited things we can do to them. We cannot add or remove items, but we can print them and find items at particular indices

# In[133]:


fruits1 = ('apple','banana','mango')
fruits1


# In[134]:


len(fruits1)


# In[136]:


fruits1[1]


# #### Tuples being immutable means that we can not alter the data inside of them. We can, however, still add tuples as we can add lists.

# In[137]:


fruits2 = ('pineapple','watermelon')
fruits3 = fruits1 + fruits2
fruits3


# #### As practice, create a tuple containing the list of days this class falls on called "classDays", and add it to another tuple with the weekdays that this class does not fall on called "daysOff". (It should create an out of order list of the 5 weekdays)

# In[138]:


classDays = ('Monday', 'Wednesday', 'Friday')


# In[139]:


daysOff = ('Tuesday', 'Thursday')


# In[140]:


weekdays = classDays + daysOff


# In[141]:


print(weekdays)


# # Part 5: Dictionaries

# #### If you recall, dictionaries are used to store key-value pairs, and you can see them in action below

# In[144]:


newDict = {"FirstName": "Gavin", "LastName": "Sidhu", "Age": 21}


# #### If you want to access a particular value, you do it similar to lists, except you want to use the key name instead of the index

# In[145]:


newDict["FirstName"]


# #### If you want to add a new key-value pair to the dictionary, you can just use a new key name and assign it a value

# In[146]:


newDict["Position"] = "Teaching Assistant"
newDict["Position"]


# #### Here are some other functions with which you can retrieve the keys, values, and items from a dictionary

# In[147]:


newDict.keys()


# In[148]:


newDict.values()


# In[149]:


newDict.items()


# #### You may also delete a key-value pair by referencing the key name 

# In[150]:


del newDict["Age"]
newDict


# #### Now, create a dictionary that contains keys "FirstName", "LastName","ClassStanding" with values corresponding to you

# In[165]:


newDict2 = {"FirstName": "Hima", "LastName": "Tulasi", "ClassStanding": "No Sitting"}


# #### Now, add 2 keys named "Age" and "StudentIDNumber" with the corresponding values

# In[166]:


newDict2["Age"] = 30


# In[167]:


newDict2["StudentIDNumber"] = 800724155


# #### Finally, remove the ClassStanding key-value pair

# In[168]:


del newDict2["ClassStanding"]


# #### Print the new dictionary

# In[169]:


print(newDict2)


# # Part 6: Sets

# #### Sets are unique and can only contain unique values. They are declared using curly braces as can be seen below

# In[171]:


numSet = {1,2,3,4,5,6,6,6,6,6,6,6,7,7,8,8,8,8,9}
numSet


# #### You can also add or remove values 

# In[172]:


numSet.add(16)
numSet


# In[173]:


numSet.remove(3)
numSet


# #### Much like in stats you can also do union or intersection operations on sets

# In[174]:


numSet2 = set(range(0,20,2))
numSet2


# In[175]:


print(numSet.intersection(numSet2))


# In[176]:


print(numSet & numSet2)


# In[177]:


print(numSet.union(numSet2))


# In[178]:


print(numSet | numSet2)


# #### Figure out how to use the range() function above to make a set called "allNumbers" with numbers from 1 to 19 (inclusive)

# In[201]:


allNumbers = set(range(0,20,1))
allNumbers


# #### Now make another set with the range() function to make a set called "evenNumbers" with even numbers from 0 through 10 (inclusive)

# In[198]:


evenNumbers = set(range(0,11,2))
evenNumbers


# #### Add the number 20 to the first set

# In[200]:


allNumbers.add(20)
allNumbers


# #### Remove 0 from the second set

# In[202]:


evenNumbers.remove(0)
evenNumbers


# #### Calculate the intersection of these sets

# In[203]:


print(allNumbers.intersection(evenNumbers))


# #### Calculate the union of these sets

# In[ ]:


p


# # Part 7: Miscellanous

# #### So far, we've seen how to do basic functions on the most common data structures, but soon, you may have to start using them in conjunction with other common programming concepts like loops, if statements, etc. When getting into Python that might require multiple lines, it is necessary to include colons. These colons indicate that the next block of code needs to be 1) indented and 2) that it is a smaller/more local block of code. It's similar to the difference between putting code inside and outside of a set of brackets in Java.

# ### Part 7.1: For Loops

# #### Here we have a regular for loop. You can set a variable name for the items in the iterable object you are trying to loop through. On each pass through the loop, that variable name holds a different value. In our case below, we named our variable "fruit", and we have it printed on each pass through the for loop as can be seen below.

# In[ ]:


for fruit in fruits:
    print(fruit)


# #### Here we have another type of for loop, in which there are two variable names being kept track of. For simplicity sake, I have named them index and element so that you can see what each keeps track of in a particular loop. When using the enumerate, the first variable name keeps track of the index as you can see below, and the second keeps track of the value at that index, or that particular element.

# In[ ]:


for index,element in enumerate(fruits):
    print(str(index) + ": " + element)


# #### One last way we can use a for loop is by setting a range. Note that the first argument is inclusive, and the second is exclusive

# In[ ]:


for num in range(0,5):
    print(num)


# ### Part 7.2: Boolean Logic/If Statements

# #### Here are a variety of boolean operations/statements. They are generally good to have in your back pocket in case you might need to use them.

# In[ ]:


className = "ITCS 3190"


# In[ ]:


className == "ITCS 3190"


# In[ ]:


className == "ITCS 3155"


# In[ ]:


className != "ITCS 3190"


# In[ ]:


className != "ITCS 3155"


# In[ ]:


"ITCS" not in className


# In[ ]:


"ITCS" in className


# In[ ]:


"3155" not in className and "ITCS" in className


# #### Now you'll see an if else statement, with the classic example of setting a system that returns your grade

# In[ ]:


grade = 91
if grade < 60:
    print('Fail')
elif grade >= 60 and grade < 70:
    print('D')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 80 and grade < 90:
    print('B')
else:
    print('A')


# ### Part 7.3: Functions

# #### If you want to define a function in Python, you must first use the keyword def, followed by the function name, followed by a set of parentheses with the arguments inside. Below is an example of a function that returns the product of two numbers a and b minus c

# In[ ]:


def productMinus(a,b,c):
    return (a*b)-c
productMinus(16,2,8)


# ### Part 7.4: Convert time to seconds

# #### For the following activity, write the function that will convert time into seconds. You will use multiple functions from python to accomplish the conversion. You shall not use any libraries or inbuilt tools. Also do not try searching google as you may end up wasting time. Just raise your hand and ask for help :)

# In[243]:


# Input is a type of String in the format --> 2:10:33 
# 2 is the hour mark, 10 is the minute mark and 33 seconds --> timeToSeconds("2:10:33") should return 7866

def timeToSeconds(time):
    timeInSeconds = sum(i * int(j) for i, j in zip([3600, 60, 1], time.split(":")))
    return timeInSeconds


# ### Part 7.5: Find largest difference in a list

# #### Given a list of Integer, return the difference between the largest and smallest integers in the list. Once again, raise your hand for any questions

# In[242]:


# maxRange([10, 15, 20, 2, 10, 6]) ➞ 18
# maxRange([3, 6, -9, -4, -2, 15]) ➞ 24

def maxRange(integerList):
    integerList.sort()
    smallest = integerList[0]
    largest = integerList[-1]
    difference = largest - smallest
    return difference

newList = [10, 15, 20, 2, 10, 6]
maxRange(newList)

