from functools import reduce

def log(x,y, result, name="sum"):
    print(f"{x} {name} {y} = {result}")
    return result

def sum(x,y):
    r = x + y
    log(x,y, r, "+")
    return r

def multiply(x,y):
    r = x * y
    log(x,y,r,"*")
    return r

def divide(x,y):
    r = x / y
    log(x,y,r,"/")
    return r

def substract(x,y):
    r = x - y
    log(x,y,r,"-")
    return r

def reduceSample():
    print("reduceSample: sum([1,2,3,4,5]) = ", reduce(sum, [1,2,3,4,5]))
    print("reduceSample: multiply([1,2,3,4,5]) = ", reduce(multiply, [1,2,3,4,5]))
    print("reduceSample: divide([1,2,3,4,5]) = ", reduce(divide, [1,2,3,4,5]))
    print("reduceSample: substract([1,2,3,4,5]) = ", reduce(substract, [1,2,3,4,5]))

reduceSample()