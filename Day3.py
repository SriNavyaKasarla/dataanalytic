# Basic in python

print("hii")
name="navya"
print("my name is",name)

  

print("MY Details")
Name=input("enter your name")
print("My name is",Name)
Age=input("enter your age")
print("My age is",Age)
address=input("Enter your address")
print("My address is",address)


# Arithmetic operators

n1 = int(input("enter n1:"))
n2=int(input("enter n2:"))
sum=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2
power=n1**2
modulus=n1%n2
floor=n1//3
print("Sum",sum)
print("sub",sub)
print("mul",mul)


# typeof 

name="navya"
print(type(name))

x=True
print(type(x))

y=7.5
print(type(y))

print("hello","navya",sep="-",end="!")

# string
str="123"
print(str)
num=int(str)
print(num)

s='My name is navya'
print(s)
print(s[1])
print(s[-3])

# list methods

a=[1,4.5,'hema',True,"hii"]
print(a)
print(a[2])
print(a[-1])
print(a[1:3])
a.append(78)
a.insert(1,'navya')
print(a)
a.remove(4.5)
a.reverse()
print(a)
a.pop()
print(a)
print(len(a))


fruits=["mango","apple"]
fruits.append("banana")
print(fruits)

# tuple methods

tup=(2,5.6,'navya',False)
print(tup)
print(tup[0])
print(tup[-2])

print(type(True))
print(type(False))
print(type(true))

# set

s1=set("hellowelcomehello")
print(s1)

s2=set(["hello","navya","hello"])
print(s2)

# string methods

str="python programming"
print(str[0])
print(str[1:3])
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.replace("python","java"))
print(str.find("programming"))
print(str.count("o"))
print(str.split())
print(str.format())

# range

numbers=range(1,15,3)
print(list(numbers))

# frozen set

fs=frozenset({1,2,3})
fs.add(4)

# dictionary

d={"name":"navya","age":22,"city":"chennai"}
print(d)
print(d["name"])
print(d["age"])
print(d["city"])

# bytes

a=[66,67,68]
print(a)

b=bytes([66,67,68]) # converts to ascci characters
print(b)

# none type

x=None
print(type(x))

y
print(type(y))
print(y)

# if-else

a=50
b=68
if a>b:
    print("a is big")
elif a==b:
    print("a and b are equal")
else:
    print("a is small")

# nested-if

i=9
if i!=0:
    print("i is non zero")
    if i>0:
        print("i is positive")
    if i<0:
        print("i is negative")
else:
    print("i is zero")

# while loop

n=5
while n>0:
    n -= 1

    if n==2:
        continue
    print(n)

# for loop

t=("apple","mango","kiwi")
for x in t:
    print(x)

x=[1,4]
y=[3,5]
for i in x:
    for j in y:
        print(i,j)


dict={"name":"apple","type":"fruit"}
for k in dict:
    print(k)

# ARRAYS

import array
fruits=array.array('u',"applebanana","hello")  #TypeError: array() takes at most 2 arguments (3 given)
print(fruits[0])
for fruit in fruits:
    print(fruit)

import array
numbers=array.array('i',[1,2,3,4,5])  # for integer case should give 'i'
length=len(numbers)
print(length)

numbers=array.array('i',[3,1,0,2,7])
sort=sorted(numbers)
print(sort)

# FUNCTIONS

def wish():
    print("good afternoon")

wish()

def greet(name):
    print("Hello",name)

greet("navya")

def add(a,b):
    return a+b

result=add(6,4)
print("sum:",result)

def greet(name="navya"):
    print("hello",name)

greet()
greet("bob")

def details():
    name="krish"
    age=20
    return name,age

n,a=details()
print("name:",n ,"| age:",a)

def add_all(*numbers):
    return sum(numbers)  # sum is pre-defined function

print(add_all(2,4,6,8))


def info(**details):
    for key,value in details.items():
        print(key,":",value)

info(name="hema",age=20,city="AP")

