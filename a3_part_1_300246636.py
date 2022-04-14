# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 3
# Year: 2021

#note: Not sure why it prints the split string twice. I only see 1 print command per condition at best.

'''
(N,d) -> (bool)
preconditions: N is a string that represents a positive integer and d is an non negative integer in string form
creates two possible outcomes depending on the d value. 
Outcome one compares two procedurally created strings and reaches a conclusion
Outcome two compares two indexes in one string and reaches a conclusion.
returns true or false
'''
def split_tester(N, d):
    p= " "
    z= " "
    d=int(d)
    if len(N)%d == 0:
        if len(N)/d > 1:
            m= " "
            for i in range(len(N)):
                if i%d==0 and i !=0:
                    m+=","                
                m+= N[i]
            print(m)
            for i in range((d*2)):
                if i < d:
                    p=p+N[i]
                else:
                    z = z+N[i]
            if p < z:
                return(True)
            else:
                return(False)
        if len(N) == d:
            print(N)
            return(True)
        else:
            m= " "
            for i in range(len(N)):
                if i%d==0 and i !=0:
                    m+=","                
                m+= N[i]
            print(m)
            if N[d-1] > N[d-2] and N[d-1] > N[0]:
                return(True)
            else:
                return(False)
    else:
        print("The given string cannot be divided by that value")
    




# main
# Your code for the welcome message goes here, instead of name="Vida"
#Creating the UI
'''
(N,d) -> (bool)
preconditions: N is a string that represents a positive integer and d is an non negative integer. Both are now manual inputs
Creates a loop to repeat the process infinitely if flag remains true
verifies many different conditions before arriving at the main function
Finally creates two possible outcomes depending on the d value. 
Outcome one compares two procedurally created strings and reaches a conclusion
Outcome two compares two indexes in one string and reaches a conclusion.
returns true or false
'''

print('*'*45)
print("*" + ' '*43 + "*")
print("* __Welcome to my increasing split tester__ *")
print("*" + ' '*43 + "*")
print('*'*45)

name= input("What is your name?: ")
l=len(name)
print("*"*(60+l))
print("*" + ' '*7 + "__"+ name+ ","+ ' '+"Welcome to my increasing split tester" +"__" ' '+ ' '*7+"*")
print("*"+' '*(58+l) +"*")
print("*"*(60+l))
print("Welcome!" + ' ' + name)
flag=True
while flag == True:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
        print("Goodbye")
    elif question == 'yes':
        print("good choice")
        N = input("Enter a positive integer: ")
        d = input("How do you want to split it? The split must evenly divide the string by it's length of "+' '+str(len(N))+ ' ')
        d = int(d)
        if float(N)%1 !=0 or float(d)%1 !=0:
            print("Sorry, we only work with integers here :)")
        elif int(N) < 0:
            print("sorry, we only want positive integers")
        else:
            split_tester(N,d)
            if split_tester(N,d) == True:
                print("It's increasing")
            else:
                print("it's decreasing")
    
    else:
        print("Try again")

