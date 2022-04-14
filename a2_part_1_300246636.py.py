# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 2
# Year: 2021
#Importing the modules needed
import math
import random

# For the elementary school quiz I first had to think of how I was going to keep track of their score in the loop while also making the loop user defined. In the end I used two more variables to iron out the bugs.
#Using the if and elif statements I made clear conditions for when the software would say each line
def elementary_school_quiz(flag, n):
    if flag == 0:
        x=0
        s=0
        while n != x:
            p =random.randint(0, 10)
            answer = input("2 to what power equals" + ' ' + str(2**p)+"?")
            if int(answer) == p:
                print("good job")
                x+=1
                s+=1
            else:
                print("unlucky")
                x+=1
        if s < n and s > 0:
            print("With a little practice you'll do fine tommorow!"+' '+name)
        elif s == n:
            print("You'll kill tomorow's test!"+' '+name)
        else:
            print("you might want some practice if you want to survive tommorow,"+' '+name)
    elif flag == 1:
        x=0
        s=0
        while n != x:
            p = random.randint(0, 10)
            answer = input("2 to the power of" + ' ' + str(p) + ' ' +  "equals?")
            a=(2**p)
            print(a)
            if int(answer) == a:
                print("good job")
                x+=1
                s+=1
            else:
                print("unlucky")
                x+=1
        if s < n and s > 0:
            print("With a little practice you'll do fine tommorow!"+' '+name)
        elif s == n:
            print("You'll kill tomorow's test!"+' '+name)
        else:
            print("you might want some practice if you want to survive tommorow,"+' '+name)





#Ironically defining the highschool function was easier minus the large strings I had to print. This was essentially all scenario creation
#Using If and Elif as well as Else and some mathematical knowledge, I recreated every single mathematical possibility when dealing with the quadratic fomula

def high_school_quiz(a,b,c):
    print("The quadratic equation:" + ' ' + str(a)+"x^2"+ ' ' + str(b)+ "x" + ' ' + str(c))
    sum = b**2 - 4*a*c
    if sum < 0:
        sum = abs(sum)
        sum = (math.sqrt(sum)/(2*a))
        print("The quadratic expression" + ' ' + str(a)+"x^2"+ ' ' + "+"+ ' '+ str(b)+ "x" + ' '+ "+"+ ' ' + str(c) + ' ' + "=0" + ' ' + "has the complex roots of:")
        print(str(a) + ' ' + "+" + ' ' + str(sum) + ' ' + "or" + ' ' + str(a) + ' ' + "-" + str(sum))
    elif a==0 and b== 0 and c==0:
        print("Every possible x value is a root for this quadratic expression")
    elif a==0:
        print("The equation,"+str(a)+"x^2"+ ' ' + str(b)+ "x" + ' ' + str(c)+ "is not a quadratic and thus has no real or possible roots.")
    elif sum == 0:
        x1 = (-b + math.sqrt(sum))/(2*a)
        x2 = (-b - math.sqrt(sum))/(2*a)
        print("The quadratic expression" + ' ' + str(a)+"x^2"+ ' ' + str(b)+ "x" + ' ' + str(c) + ' ' + "=0" + ' ' + "has one root:")
        print(x1)
    else:
        x1 = (-b + math.sqrt(sum))/(2*a)
        x2 = (-b - math.sqrt(sum))/(2*a)
        print("The quadratic expression" + ' ' + str(a)+"x^2"+ ' ' + str(b)+ "x" + ' ' + str(c) + ' ' + "=0" + ' ' + "has 2 real roots:")
        print(str(x1) + ' ' + "and" +' ' + str(x2))







# main
#Creating the UI
print('*'*41)
print("*" + ' '*39 + "*")
print("* __Welcome to my math quiz-generator__ *")
print("*" + ' '*39 + "*")
print('*'*41)
#Asking for the ever important name so that I can use it's length to custimize the UI the rest was to use the blocks already laid out to form the program.

name=input("What is your name? ")
l=len(name)
status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")
if status=='1':
    print("*"*(60+l))
    print("*" + ' ' + "__"+ name+ ","+ ' '+"Welcome to my math quiz-generator for elementary!" +"__" ' '+ ' '+"*")
    print("*"+' '*(58+l) +"*")
    print("*"*(60+l))
    print("Welcome!" + ' ' + name)
    flag=input("What would you like to practice? Type 0 for logorithmic practice, 1 for exponent practice or anything elsefor closing the program ")
    n=input("How many questions do you want to do? Choose between either 1 or 2. Any other input will close the program.")
    flag=int(flag)
    n=int(n)
    elementary_school_quiz(flag,n)
elif status=='2':
    print("*"*(39+l))
    print("*"+' '+"__Quadratic Equation solver for,"+' '+name+"__"+' '+"*")
    print("*"+' '*(37+l) +"*")
    print("*"*(39+l))
    print("Welcome!" + ' ' + name)
    flag=True
    while flag==True:
        question=input(name+", would you like a quadratic equation solved? ")
        if question != "yes":
            flag=False
        else:
            print("Good choice!")
            a=input("what is the first coeficcient?:")
            b=input("what is the second coeficcient?:")
            c=input("What is the third coefficient?:")
            a=int(a)
            b=int(b)
            c=int(c)
            high_school_quiz(a,b,c)
else:
    pass

print("Good bye "+name+"!")
