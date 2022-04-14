# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 6
# Year: 2021

from os import error, read
import string
from typing import Union

#helper function #1
def remove_punctuation(line):
    '''
    str -> str
    get's rid of punctuation in given string
    '''
    newline=""
    for i in line:
        if (i in "'?!.,-") == False:
            newline+=i.lower()
    return(newline)

#helper function #2
def remove_allpunctuation(text):
    '''
    list -> list
    get's rid of all punctuation using the function remove_punctuation.
    precondition:
    list needs to be of string values
    '''
    newtext=[]
    for i in range(len(text)):
        line=text[i]
        newtext.append(remove_punctuation(line))
    return(newtext)

#helper function #3

def no_numbers(newtext,newertext):
    '''
    (list,empty dictionary) -> dictionary
    takes in a list and forms a dictionary out of it
    '''
    for i in range(len(newtext)):
        checked_text=newtext[i].split()
        h=i
        for i in range(len(checked_text)):
            if checked_text[i].isalpha()==True and (len(checked_text[i]) >= 2):
                if (checked_text[i] in newertext) == False:
                    a=set()
                    a.add((h+1))
                    newertext[(checked_text[i])]=a
                else:
                    a=newertext[(checked_text[i])]
                    a.add((h+1))
                    newertext[(checked_text[i])]=a
    return(newertext)

#helper function #4
def isvalid(D,query):
    '''
    (dict,str) -> bool
    takes in dictionary and string values and checks to see if the string value is applicable.
    
    '''
    query=query.split()
    check=True
    i=0
    if len(query) == 0:
        check=False
    while check == True and i < len(query):
        try:
            D[query[0]]
            check = True
        except:
            print("Word '"+(query[i])+"'"+' '+ "is not in file.")
            check = False
        i+=1
    return(check)

    


def open_file():
    '''None->file object
    See the assignment text for what this function should do
    '''
    # YOUR CODE GOES HERE
    check = False
    file = input("Which file will you open? ")
    while check == False:
        try:
            text = open(file).read().splitlines()
            check = True
        except:
            print("try again.")
            file = input("Which file will you open? ")
    return(text)

#text=(open_file())

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do
    '''
    # YOUR CODE GOES HERE
    #text=open_file()
    newtext=remove_allpunctuation(fp)
    newertext=dict()
    newertext=no_numbers(newtext,newertext)
    return(newertext)

#newertext=read_file(text)
#query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do
    '''
    # YOUR CODE GOES HERE
    check = isvalid(D,query)
    query=query.split()
    if check == False:
        pass
    else:
        if len(query) == 2:
            results= (D[query[0]]).intersection((D[(query[1])]))        
        elif len(query) == 1:
            results = (D[query[0]])
        return(list(results))


##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
while query != 'q':
    print(find_coexistance(d,query))
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

