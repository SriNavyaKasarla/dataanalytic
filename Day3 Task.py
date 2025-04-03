# Tuple methods
tup=(5,6.8,5,5,3,2)
print(tup)
print(tup.index(3))
print(tup.count(5))
print(min(tup))
print(max(tup))
print(sum(tup))
print(sorted(tup))
print(len(tup))


# Grading

a =int(input("Enter average: "))
if a>=90 and a<=100:
    print("Grade A")
elif a>=70 and a<=80:
    print("Grade B")
elif a>=60 and a<=70:
    print("Grade C")
else:
    print("Fail")


#reverse and check palindrome

str=input("enter string: ")
rev=str[::-1]
print(rev)
if str==rev:
    print("string is palindrome")
else:
    print("string is not a palindrome")


#prime number

n = int(input("enter a number: "))
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")


#Fibinocci series

a=0
b=1
for i in range(1,10):
    c=a+b
    print(c)
    a=b
    b=c


#even or odd

n=int(input("enter a number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")


#even number change to @

for i in range(1,100):
    if i%2==0:
        print(i)
        print("@")


# iterate each element and square it

n=[4,6,9,5]
for x in n:
    print("number: ",x)
    print("square:",x*x)
 

#Retrieving keys from dict and displaying values based on keys

dict = {"name":"Navya","Age":22,"city":"Chennai","course":"Data analytic"}
for details in dict:
    print(details)
print("key values: ")
print(dict["name"])
print(dict["Age"])
print(dict["city"])
print(dict["course"])


# creating a function to get user details from user , using another function to display the value

def getdata():
    name=input("enter your name: ")
    age=input("enter your age: ")
    address=input("enter your address:")
    return name,age,address

def display(name,age,address):
    print("User details:")
    print("Name: ",name)
    print("Age: ",age)
    print("Address: ",address)

name,age,address=getdata()
display(name,age,address)