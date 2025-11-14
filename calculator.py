import math
def add(a, b):
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    try:
        b / a
    except:
        raise ZeroDivisionError
# raise ZeroDivisionError if a == 0

def log(a, b):
    try:
        math.log(a,b)
    # use math library + raise ValueError
    except:
        raise ValueError
def exp(a, b):
    math.pow(a,b)
