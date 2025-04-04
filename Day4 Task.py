# Types of Inheritance
# 1.single inheritance
class Parent:
    def display(self):
        print("parent class")
class Child(Parent):
    def name(self):
        print("child name")
        print("Hema")
obj = Child()
obj.display()
obj.name()

#2.Mutliple Inheritance

class one:
    def method1(self):
        print("class one")
class two:
    def method2(self):
        print("class two")
class three(one,two):
    def method3(self):
        print("class three")
obj1=three()
obj1.method1()
obj1.method2()
obj1.method3()

#Multi-Level Inheritance

class A:
    def dis(self):
        print("class A")
class B(A):
    def dis1(self):
        print("class B")
class C(B):
    def dis2(self):
        print("class C")
obj2=C()
obj2.dis()
obj2.dis1()
obj2.dis2()

#Hierarchical inheritance

# Base class
class Animal:
    def speak(self):
        print("Animals sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks: woof!")

class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow!")

dog = Dog()
cat = Cat()
dog.speak()   
dog.bark()    
cat.speak()   
cat.meow()    


# Overloading and overriding
class Sample:
    def show(self):
        print("No arguments")

    def show(self, a):
        print("One argument:", a)

    def show(self, a, b):
        print("Two arguments:", a, b)

obj = Sample()
obj.show(10, 20)

#overriding
class Parent:
    def greet(self):
        print("Class - Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Class - Child")

c = Child()
c.greet()  


# Encapsulation - hiding internal details and protecting data

class Student:
    def __init__(self, name, age):
        self.name = name  
        self.__age = age   

    def get_age(self):
        return self.__age  

s = Student("Alice", 20)
print(s.name)        
print(s.get_age())   
#print(s.__age)     # error - no attribute

# Polymorphism

class Pen:
    def write(self):
        print("Writing with a pen")

class Pencil:
    def write(self):
        print("Writing with a pencil")

def start_writing(tool):
    tool.write()

p1 = Pen()
p2 = Pencil()
start_writing(p1)   
start_writing(p2)   




