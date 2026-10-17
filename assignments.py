'''num1= int(input('enter first number:'))
num2= int(input('enter second number:'))
result = num1+num2
print('addition:',result)

num1= int(input('enter first number:'))
num2= int(input('enter second number:'))
result = num1-num2
print('subtraction:',result)

num1= int(input('enter first number:'))
num2= int(input('enter second number:'))
result = num1*num2
print('multiplication:',result)

num1= int(input('enter first number:'))
num2= int(input('enter second number:'))
if num2 !=0:
    result= num1 / num2
    print('division:',result)
else:
    print('cannot divide by zero')

num1= int(input('enter first number:'))
jl= input('enter operator(+,-,*,/):')
num2= int(input('enter second number:'))

if jl == '+':
    print('addition:',num1 + num2)
elif jl == '-':
    print('subtraction:',num1 - num2)
elif jl == '*':
    print('multiplication:',num1*num2)
elif jl =='/':
    if num2 !=0:
        print('division:',num1 / num2)
    else:
        print('cannot divide by zero')

else:
    print('invalid operator')


task = input('enter your task:')
print('your task is:',task)

tasks = ['learn python','practice coding','complete homework']
print(tasks)


tasks = ['learn python','practice coding','complete homework']
tasks.append('read a book')
print(tasks)

tasks = ['learn python','practice coding','complete homework']
new_task = input('enter a new task:')
tasks.append(new_task)
print('my to-do list:',tasks)

tasks = ['learn python','practice coding','complete homework']
for task in tasks:
    print(task)

tasks = ['learn python','practice coding','complete homework']
tasks.remove('learn python')
print('updated to-do list:',tasks)


tasks = ['learn python','practice coding','complete homework','read a book']
completed_task = input('enter the completed task:')
if completed_task in tasks:
    tasks.remove(completed_task)
    print('task removed successfully!')
else:
    print('task not found!')
print('remaining tasks:',tasks)

tasks = ['learn python','practice coding','complete homework']
print('total tasks:',len(tasks))

tasks = ['learn python','practice coding','complete homework']
tasks.append('read a book')
print('updated tasks:',tasks)
print('totaltasks:',len(tasks))

#GENERATE A  PASSWORD USING LETTERS ONLY.   
import random
import string
characters = string.ascii_letters
password =''
for i in range(8):
    password += random.choice(characters)
print('password:',password)

#GENERATE A  PASSWORD USING NUMBERS ONLY.
import random
import string
characters = string.digits
password = ''
for i in range(6):
    password += random.choice(characters)
print('password:',password)


#GENERATE A  PASSWORD USING LETTERS AND NUMBERS ONLY.
import random
import string
characters = string.digits + string.ascii_letters
password = ''
for i in range(10):
    password += random.choice(characters)
print('password:',password)'''

#LET THE USER CHOOSE THE PASSWORD LENGTH
import secrets
import string
characters = string.digits + string.ascii_letters + string.punctuation
length =  int(input('enter password length:'))
password = ''
for i in range(length):
    password += secrets.choice(characters)
print('generate password:',password)
