#coding=utf-8

__author__= "Daniel"
__author_email__= "danielliu2000@hotmail.com"

import sys



def Sum2Num(a,b):
    """
    Given two number a and b, plus them and return the value
    """
    sum = a + b
    return sum


if __name__ == '__main__':

    try:
        num1=float(sys.argv[1])
        num2=float(sys.argv[2])

    except(IndexError,ValueError) as e:
        print("You must input two numbers as parameters ")
        print("Example: python Sum2Num.py 3 5")
        sys.exit(1)


    result=Sum2Num(num1,num2)
    print(result)


