import os # importing the os module 
# MODULES: A module is a file written by someone else, which can be imported and used by us in our programs(e.g. OS, tensorflow......)

# PRINT HELLO WORLD IN PYTHON

print("Hello world")

# Print the contents of a directory
print(os.listdir)

# VARIABLES AND DATATYPES
 a=input("enter first number: ")
  square=a*a
  print("square of a is:" square)
  
#String is a data type in python
#String is sequrnce of charcters enclosed in quotes
a='saif'
b="saif"
c='''saif'''

b = '''Saif"s and 
       Saif's'''
print(b)

'''String Slicing: A string in python can be sliced for getting a part of the string'''
'''The index in a string starts from 0 to (length-1), in python''' 
name="Saif"
print(name[2])
#output:i

greeting="hello,"
c=greeting+saif    #concatination
# name[3]='d', ERROR, String is not mutable
print(name[0:3])# 3 is excluded
print(name[:3] # is same as name[0:3]
print(name[0:]#is same as name[0:last index]

# Negative index: starts from the end -1, goes like -1, -2, -3,..... from last to first elemen
c=name[-4:-1]#same as name[0:]
'''slicing with skip value'''
word="amazing"
word[1:6:2] # output: mzn, print every second character
word[1::2]

Story="Once Upon a time there was the chief god of universe....... IYKYK"
# STRING FUNCTIONS

print(len(Story))
print(Story.endswith("IYKYK"))
print(Story.count("O"))

print(Story.capatilize()) #Capitalizes the first word
print(story.find("Once"))
print(story.replace("Once","One")

#ESCAPE SEQUENCE CHYARACTERS

#\n next line
#\t tab space
# \' single quote
# \\ backslash

#CHAPTER 4
#LIST AND TUPLES

'''Python lists are containers to store values of any type'''

a=[1,2,3,4,6]
print(a[2])
#index for list starts at 0

a[0] =98

print(a)
 '''We can create a list with items of different types'''
C=[45,"Saif", False,6.9]
print(C[0:3]) # Slicing of list
print(C[-3:])


L1=[1,2,3,7,5,,6,90,8]
#lists are mutable

L1.Sort()
L1.reverse()
L1.append(9)#adds at the end of list
L1.insert(3,8) #inserts 8 at index 3
L1.pop(2)# Reomve from index 2

#TUPLE
t=(1,2,3,4)
'''Tuple is not mutable'''
      
t1=(1) # wrong way to declare a tuple with single element
t1=(1,)#Tuple with single element
 print(t.count(1)) # count no of occurence of 1
print(t.index(1)) # return index of 1     
 
      




      
      
      
      
      
      
      
      














