#variable and its address
num=5
id(num)

#relational and logical operator
i=1
while i<=100:
    if ((i%3 and i%5)!=0):
        print(i)
    i=i+1

# Lists
list = []
  
# Adding Element into list
list.append(5)
list.append(10)
print("Adding 5 and 10 in list", list)
  
# Popping Elements from list
list.pop()
print("Popped one element from list", list)
print()
  
# Set
s = set()
  
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
  
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

set1 = set([1, 2, 4, 4, 3, 3, 3,6, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

set1 = set([ 4, 5, (6, 7)])
set1.update([10, 100])
print("\nSet after Addition of elements using Update: ")
print(set1)
  
# Tuple
t = tuple(l)
  
# Tuples are immutable
print("Tuple", t)
print()

#remove iteams from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#nested tuple
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('u', 'p')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))


#unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
  
# Dictionary
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict["brand"])


d = {}
  
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
  
# Removing key-value pair
del d[10]
print("Dictionary", d)

#converting list into dictionary
names = ["vikrant","anmol","pradeep","pratiksha"]
num=[1,2,3,4,5]
data= dict(zip(names,num))
data

#list and dictionary in dictionary
prog={'js':'atom','cs':'vs','python':['vs','pycham'],'java':{'jse':'netbeans','jee':'eclipse'}}
prog
prog['java']


#input and output print greatest no

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print("A is greatest")
elif y>c:
    print("b is greatest")
else :
    print("c is greatest")
#or

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
#d=int(input("enter the number"))

print("the maximum value is :" , max(a,b,c))

#nested if and odd and even no

a= int(input("enter no"))
x = a%2
if (x==0):
    print("Even no")
    if(a<5):
        print("NO IS SMALLER THAN 5")
    else:
        print("NO is greater than 5")
else:
    print("Odd no")



#Array
from array import *
vals= array("i",[45,55,69,71,45])
print(vals)

#for character input
vals=array('u',['a','e','i'])
for e in vals:
    print(e)

#buffer_info() - Return a tuple (address, length)

from array import *
vals= array("i",[45,55,69,71])
print(vals.buffer_info())

#reverse an array

from array import *
vals= array("i",[45,55,69,71])
vals.reverse()
print(vals)
print(vals[2])

#creating new array with existing array element

vals=array('i',[5,6,4,8,5])
newArr = array(vals.typecode,(a*a for a in vals))
for i in newArr:
    print(i)

#enter user input
arr=array('i',[])
n=int(input("enter the length of the array"))

for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)
print(arr)

#enter input from user in array and search for entered element

from array import *
arr=array('i',[])
val=int(input("Enter the length of the value"))

for i in range(val):
    n=int(input("Enter the next value :"))
    arr.append(n)
print(arr)

no=int(input("enter the number you want to search :" ))

k=0
for e in arr:
    if e==no:
        print(k)
        break
    k=k+1
