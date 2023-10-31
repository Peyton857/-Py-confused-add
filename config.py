#Made by PeytonGaming562
import random
import math
#changes the python code functions:
Rand = random.randint(1,10)
Ran = random.randint
Ra = random
Fe = False
In = input
Po = print
Te = True
Il = int
Res = "result:"
Rag = range
_ = "."
#Adds custom functions:
def set(GH, HJ):
  GH = HJ
  return GH
def Loop(string):
  for i in range(10):
    print(string)
def DB(decimal_number):
  binary_number = ""
  while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2
  return binary_number
def add(Numb1, Numb2):
  return Res,Numb1 + Numb2
def sub(Numb1, Numb2):
  return Res,Numb1 - Numb2
def mul(Numb1, Numb2):
  return Res,Numb1 * Numb2
def div(Numb1, Numb2):
  return Res,Numb1 / Numb2