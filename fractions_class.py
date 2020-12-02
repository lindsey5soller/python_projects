# -*- coding: utf-8 -*-
"""Fractions_Class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZ8Q00G5OWsgxCrq6Y3BB3Ca9r44YLDn
"""

##This document is a fractions class that will be used for simpler operations on fractions that return fractions

#Crete fractions class
class Fraction():
  #initalize class with numberator and denomerator
  def __init__(self, num, den):
    self.num = num
    self.den = den

  #This is what you get with print()
  def __str__(self):
    return f'{self.num}/{self.den}'

  #This is what you get with + (adding 2 numbers)
  def __add__(self, frac2):
    new_den = self.den * frac2.den
    new_num = self.num * frac2.den + frac2.num * self.den
    new_frac = Fraction(new_num, new_den)
    return f'{new_frac}'

  def reduce(self):
    num = self.num
    den = self.den
    divisor = self.gcd()
    new_num = int(self.num / divisor)
    new_den = int(self.den / divisor)
    new_frac = Fraction(new_num, new_den)
    return f'{new_frac}'    



  def gcd(self):
    a = self.num
    b = self.den
    if a == 0:
      return b
    if b == 0 :
      return a
    self.num = b
    self.den = a % b
    return self.gcd()




#Create new sub class that inhearts all the properties from Fraction
class Mixed(Fraction):


  def __init__(self, whole, num, den):
    self.whole = whole
    self.num = num
    self.den = den


  def __str__(self):
    return f'{self.whole} {self.num}/{self.den}'

  def improper(self):
    new_num = self.den * self.whole + self.num
    new_den = self.den
    return f'{Fraction(new_num, new_den)}'


  def __add__(self, frac2):
    return self.improper() + frac2.improper()



print('''This is a fractions class in progress

        1. Intitalize Fraction
          one half = Fraction(1, 2)
        2. Add fractions 
          one_half + one_half
        3. Display fractions
          print one_half ''')


#f1 = Mixed(3, 1, 2)
#1/2 +1/3
#3/6 + 2/6
#n1/d1 + n2/d2 = (n1d2 + n2d2)/d1d2

'''
f1 = Mixed(3, 1, 2)
print(f1.improper())
'''

'''
f2 = Fraction(8, 12)
print(f2.reduce())
'''

'''
third = Fraction (1, 3)
half = Fraction (1, 2)
forth = Fraction (1, 4)
print(half + third)
print(half + Fraction(2, 5))
'''

def fact(n):
  n == abs(n)
  if n == 1:
    return 1
  else:
    return n * fact(n-1)

print(fact(4))
