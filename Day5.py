
#JSON
import json

# json to python
X='{"name":"navya","age":22}'
z=json.loads(X)
print(z["name"])
print(z["age"])

#dictionary to json format
x={"name":"mark","age":35}
y=json.dumps(x)
print(y)

#REGEX - regular expression

import re
u="The rain in spain"
v=re.search("^The.*spain$",u)
if v:
    print("yes the match is correct")
else:
    print("Not matching with pattern")
#findall
Y=re.findall("ai",u)
print(Y)
#split - \s used to split with white spaces
M=re.search("\s",u)
print(M)
Z=re.split("\s",u)
print(Z)
K=re.sub("\s","$",u)
print(K)

pattern=r"\d+"
text="there are 122 apples"
match=re.search(pattern,text)
if match:
    print("Match found:",match.group())


pattern=r"\d+"
text="there are 125 apples and 450 oranges"
matches=re.findall(pattern,text)
print(matches)


pattern=r"(\d+)-(\d+)-(\d+)"
text="the event is on 2025-03-26"
match=re.search(pattern,text)
if match:
    print("Year:",match.group(1))
    print("Month:",match.group(2))
    print("day:",match.group(3))


import re
#email validation
email_pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text="Please contact us at navya@gmail.com"
match=re.search(email_pattern,text)
if match:
    print("Email found:",match.group())


#Logging - we can trace out the issue in our project


import logging
logging.basicConfig(level=logging.DEBUG) 

logging.debug('hello,debug!')
logging.info('hello,info!')
logging.warning('warning!')
logging.error('error!')
logging.critical('critical!')


import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'
)
logging.debug('hello,debug!')
logging.info('hello,info!')
logging.warning('warning!')
logging.error('error!')
logging.critical('critical!')



try:
    x=10/0
except ZeroDivisionError:
    print("divide by zero")
finally:
    print("completed execution")



try:
    num=int(input("enter a number"))
    result=10/num
except ValueError as e:
    print("invalid input",e)
except ZeroDivisionError as e:
    print("cannot divide by zero")
except Exception as e:
    print("unexpected")
else:
    print("Result: ",result)
finally:
    print("code executed successfully")




def checkage(age):
    if age<18:
        raise ValueError("age must be 18")
    else:
        print("you are eligible")
try:
    checkage(16)
except ValueError as e:
    print("error: ",e)



# creating exceptions

class noteligible(Exception):
    pass
def check(age):
    if age<18:
        raise noteligible("age must be 18")
    else:
        print("you are eligible")
try:
    check(16)
except noteligible as e:
    print("error: ",e)


file=open('test.txt','r')
content=file.read()
print(content)                     #print("hello world")! navya hema
content1=file.readline()     
print(content1)            #print("hello world")!
content2=file.readlines()  
print(content2)     #['print("hello world")!\n', 'navya\n', 'hema']
file.close()

file=open('test.txt','w')
file.write("hello navya\n")
file.write("good bye")


import os   # checking if particular file existing in our system or not   , we can only check it by using os only
if os.path.exists('test.txt'):
    with open('test.txt','r')as file:
        content=file.read()
        print(content)
else:
    print("file does not exist")




import os
try:
    with open('test.txt','r') as file:
        data=file.read()
    with open('test.txt','w')as filewrite:
        filewrite.write(data)
    print("file copied successfully")

except FileNotFoundError:
    print("input or output opeation file")
except IOError as e:
    print(e)
except Exception as e:
    print("unexpected error")

f=open('example.txt','x')
os.remove("test.txt")  #removes file in the existing system
os.mkdir("myfolder")   #creates the folder
os.rmdir("myfolder")   #removes the folder


#pylint 
import pylint
for num in range(1,10):
    print(num)

    

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="navya"
)
print(conn)

cursor=conn.cursor()

cursor.execute("select * from DataRevature.student")
for row in cursor:
    print(row)
