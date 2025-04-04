#lamda function
s1="hello good morning"
s2=lambda func:func.upper()
print(s2(s1))

n = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(n(6))
print(n(-3))
print(n(0))


sq = lambda x: x**2    # using lambda function it is in one line 
print(sq(3))

def sqdef(x):    # using function  
    return x**2
print(sqdef(3))



li = [lambda arg=x: arg*10 for x in range(1,5)]  #arg is used here to return back the value
for i in li:
    print(i())    # without braces it will not be in a readable format




check = lambda x: "Even" if x%2==0 else "Odd"   # In lamda we can not use elif
print(check(6))
print(check(1))  




#lambda with multiple statements
calc = lambda x,y: (x + y, x * y)
result=calc(5,7)
print(result)   # returns the output in tuple format



n=[5,6,7,8,9]
even=filter(lambda x: x%2 == 0,n)  #filter applies the condition and returns only the values which satisfies the condition
print(even)   # non-readable format
print(list(even))



a=[1,2,3,4]
b=map(lambda x: x*2,a)   # map iterates through a and applies the transformation
print(list(b))



from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y: x*y,a)   #reduce applies this operation across list
print(b)     



# string format types
a="Navya"
b=22

msg="My name is {0} and I am {1} years old".format(a,b)
print(msg)

##########
a="python"
print("This article is written in {}".format(a))

print("Hi, My name is {} and I am {} years old".format("hema",20))


#fstring

name="Bob"
age=25
print(f"Hello,My name is {name} and I am {age} years old")




# Inner class used to hide the logic from external access

def fun1(msg):      #Outer function
    def fun2():     #inner function
        print(msg)
    fun2()
fun1("hello")




#decorator

import inspect

def decorator(func):

    def wrapper():
        print("before calling the function")
        func()
        print("After calling the function")
    return wrapper

#Applying the decorator to a function
@decorator     #greet = decorator(greet)

def greet():
    print("Hello world")
greet()

print(inspect.signature(decorator))



# Class and Object


class Dog:
    sound = "bark"

dog1= Dog()       # creating object to the class
print(dog1.sound) # accessing the class attribute



# using __init__() function
#it automatically initializes object attributes when an object is created

class Dog:
    species ="Canine"

    def __init__(self,name,age):    # self is a reference to the current instance of the class
        self.name=name
        self.age=age

dog1=Dog("Buddy",4)

print(dog1.name)
print(dog1.species)



class Dog:

    def __init__(self,name,age):    # self is a reference to the current instance of the class
        self.name=name
        self.age=age

    def __str__(self):     # print the pbject like toString()   
        return f"{self.name} is {self.age} years old"

dog1=Dog("Buddy",4)
dog2=Dog("snoopy",7)

print(dog1)
print(dog2)




class Dog:
    species = "Canine"

    def __init__(self,name,age):    # self is a reference to the current instance of the class
        self.name=name
        self.age=age

dog1=Dog("Buddy",4)
dog2=Dog("snoopy",7)

print(dog1.species)
print(dog1.name)
print(dog2.name)


dog1.name="Max"
print(dog1.name)

Dog.species="Feline"
print(Dog.species)


# inheritance

class Teacher:
    def __init__(self,name):
        self.name=name

    def name(self):
        return "remya"    

class Student(Teacher):
    def subject(self):
        return "python"
    
t=Teacher("python trainer")

s=Student("Navya")

print(t.name)
print(s.name)
print(s.subject())



class Color:    #outer class

    def __init__(self):
        self.name='Green'
        self.lg=self.Lightgreen()

    def show(self):
        print('Name:',self.name)

    class Lightgreen:

        def __init__(self):
            self.name='Lightgreen'
            self.code='024avc'

        def display(self):
            print('Name:',self.name)
            print('Code:',self.code)

outer = Color()   # outer class object creation
outer.show()       # outer class method invocation

g=outer.lg      # inner class object creation
g.display()     #inner  class method calling   # example - college and department , without battery no use of remote




# super keyword

class Parent():
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Inside Child")

obj=Child()
obj.show()



class private:
    def __init__(self):
        self.__salary=60000  #private attribute double underscore

    def salary(self):
        return self.__salary   # access through public method

obj = private()
print(obj.__salary)   # raises attribute error
print(obj.salary())   # works




# iter()

num=[1,2,3,4,5]
iter_num=iter(num)    # iter function creates an iterator object from num list
print(next(iter_num))  # next function used to retrieve elements from iterator sequentially
print(next(iter_num))


# local scope

def myfunc():
    x=100
    print(x)
myfunc()


# enclosing scope 

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# global scope

x=200

def myfunc():
    y=50
    print(x)
    print(y)
myfunc()

print(x)
# print(y)   outside the function so it can not access the value


# math library

import math

y = math.pow(3,4)
print("power of y : ",y)

z=math.floor(4.8)
print("floor value : ",z)

x=math.sqrt(81)
print("square root of 81: ",x)

a=math.ceil(6.3)
print("ceil of 6.3 is: ",a)



# importing other file in present file

def wish():
    print("hello")
def greet():
    print("good afternoon")

import module1

module1.wish()
module1.greet()



# numpy 

import numpy as np

arr=np.array([1,2,3])
print(arr)
print(type(arr))    #<class 'numpy.ndarray'>

z=np.zeros((2,3))
print(z)
o=np.ones((3,2))
print(o)
a=np.arange(0,10,2)
print(a)
l=np.linspace(0,1,5)
print(l)
r=np.random.rand(2,2)
print(r)



a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a*b)
print(a**2)
print(np.sqrt(a))


A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,3]])

print(np.dot(A,B))   # matrix multiplication
print(np.transpose(A))
print(np.linalg.inv(A))   #inverse (if A is invertible)


arr=np.array([[10,20,30],[40,50,60]])
print(arr[0,1])
print(arr[:,1])
print(arr[1])

arr=np.array([1,2,3,4])
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.max())
print(arr.min())



# pandas

import pandas as pd

# u=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print(u)

data={
    'Name':['alice','bob','charlie'],
    'Age':[25,30,40],
    'City':['New York','Paris','London']
    }

df=pd.DataFrame(data)    # framing the data in a structured way
print(df)

#df.head()
#df.tail(2)
df.info()
#df.describe()
df.columns
df.shape


print(df['Age'])      # select a column

print(df[['Name','City']])     # selects multiple columns

print(df[df['Age']>28])    # filter rows



df['Age']+=1        #modifies the column

df['Country']='USA'     # adds new column

df.rename(columns={'Age':'Years'},inplace=True)

df.drop('City',axis=1) #drop column
print(df)
