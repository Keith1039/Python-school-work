# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 3
# Year: 2021
import math 
#done 2.1

'''
(string)-> a number(y)
preconditions: n is a number
returns sum of all positive odd divisors of inputed number n
'''

def sum_odd_divisors(n):
    n = int(n)
    if n == 0:
        pass
    else:
        y=0
        n=abs(n)
        for i in range(1,n+1):
            if n % i  == 0 and i%2 != 0:
                y+=i
        return(y)


#Done 2.2
'''
()-> a number(y)
preconditions: inputed string is a number.
returns a number y when given the input n
'''

def series_sum():
    n = input("please enter a non-negative integer number:")
    n= int(n) + 1
    if int(n) < 0:
        pass
    elif int(n)-1 == 0:
        y=1000
    else:
        y=1000
        for i in range(int(n)):
            if i > 0:
                y+=(1/(i)**2)
    return(y)


'''
def pell(n):
    p=0
    for i in range(n):

    return(p)
print(pell(3))
'''



#2.4 done
'''
#(str)-> integer (x)
#preconditions: The value s is a string value 
#returns value of x as an integer when certain conditions are fufilled
'''

def countMembers(s):
    x=0
    for i in s:
        if i in '!,\FXGHIJKLMNOPQRSTUVWefj23456':
            x+=1
    return(x)




#Done 2.5
'''
(str)-> string(s)
precondtion: input s is a string
returns a reformed string with the value of s1
'''
def casual_numbers(s):
    for i in s:
        if  ord(i) > 64 and ord(i) < 123:
            check= False
            break
        else:
            check =True
    if check == True:
        s1=" "
        for i in s:
            if i == "-":
                s1+=i
            if i.isdigit() == True:
                s1 += i
        return(s1)
    else:
        pass


#done 2.6
'''
(string)->(int)
precondtion: s is a string
returns value of the string(s) if as conditions are fufileld
'''

def alien_Numbers(s):
    return((s.count("T")*1024 + s.count("y")*598 + s.count("!")*121 + s.count("a")*42 + s.count("N")*6 + s.count("U")*1))


#Done 2.7
'''
(str)->(int)
precondition: s is a string
returns y value of the string(s) if certain conditions are achieved
'''

def alien_Numbers_Again(s):
    y=0
    for i in s:
        if i == "T":
            y+=1024
        elif i == "y":
            y+=598
        elif i == "!":
            y+=121
        elif i == "a":
            y+=42
        elif i == "N":
            y+=6
        elif i == "U":
            y+=1
    return(y)

'''
(str)->(str)
preconditions: s must be a string
returns a newly formed string with indexing
'''
def encrypt(s):
    p=" "
    s= (s[::-1])
    for i in range(len(s)): 
        p+=s[i]
        i+=1
        p+=s[-i]
        if i >= (len(s)/2):
            break
    return(p)



