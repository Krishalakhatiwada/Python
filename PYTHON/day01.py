#python variable
#we don't need to define variable in python:dymnamic
#typed language so its interpreter detects the variable during runtime
var1=23
var2='nice'
print("type of var1:",type(var1))
print("type of var2:",type(var2))
var4='name'
print("type of variable",type(var4))
var4=234
print("var4=",var4)
print("type of variable",type(var4))
#comma operator in python adds a space between values of two variables
#+(plus) operator doesn't add values between two variables

#Types of variables
#1. Global Variable:
 #has larger scope and can be accessed from any part of the program
#Local Variable : 
#                Has very small scope and is accessible only in the part of section of the program where it is defined in.


#y='c'
#print(type(y))
#print(type(z))
#print(z)
x=-87.346#int
y=12E4 #float
z=1j #complex
print(type(x))
print(type(y))
print( type(z))
print(x)
print(y)
print(z)
print(x+y)
#user input in python
name= input("enter your name")
print ("your name is:", name)
number=  int (input("enter a number"))
print("the number is:",number)
import math
math.cos(1)
math.ceil(2.3)
math.floor(2.6)
math.tan(1)

#from radian to degree
math.degrees(1)
#find exponential of specific value
print(math.exp(1))
#remove sign of given number
#print(math.fab(-66.24))
math.factorial(2)
math.gcd(55,5)
math.log2(1024)
math.e
math.pi 
math.inf
import random
print(random.randint(2,8))


#random
#return a number between 3 and 9 (both included)
print(random.radian(3,9))

a=[1,2,3,4,5,6,7,8]
print(a)
#Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers