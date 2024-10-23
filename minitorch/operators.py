"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a,b):
    return a*b

def id(a):
    return a

def add(a,b):
    return a+b
def neg(a):
    return -1*a
def lt(a,b):
    return a<b
def eq(a,b):
    return a==b
def max(a,b):
    if(a>b):
        return a
    return b
def is_close(a,b):
    delta=abs(a-b)
    return  delta<1e-2
    
def sigmoid(x):
    return 1.0/(1.0+math.e**(-1*x))        
def relu(x):
    if x>0:
        return x
    return 0.0
def log(x):
    return math.log(x)
def exp(x):
    return math.e**x


def inv(x):
    return 1/x

def log_back(a,b):
    return b*inv(a)

def inv_back(a,b):
    return b*(-1*inv(a)**2)
def relu_back(a,b):
    if a>0:
        return b
    return 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(f,iterable):
    return [f(x) for x in iterable]

def zipWith(f,a,b):
    return [f(i,j) for i,j in zip(a,b)]
    
def reduce(f,iterable,initial):
    it = iter(iterable)
    
    # If no initial value is provided, use the first item of the iterable
    if initial is None:
        value = next(it)
    else:
        value = initial
    for element in it:
        value = f(value, element)
    
    return value

def negList(lst):
    return map(lambda x:-1*x,lst)

def addLists(lst1,lst2):
    return zipWith(lambda x,y:x+y,lst1,lst2)

def sum(lst):
    return reduce(lambda x,y:x+y,lst,0)

def prod(lst):
    return reduce(lambda x,y:x*y,lst,1)


