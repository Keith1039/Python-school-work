# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 2
# Year: 2021

#Once the question was understood I used a quick if,else statement to make sure that the radius would be positive
#By subtracting each coordinate value by the radius the rectangle is the smallest possible one but it always encloses the circle
def min_enclosing_rectangle(radius, x, y):
    if radius > 0:
        x=x-radius
        y=y-radius
        return(x,y)
    else:       
        pass
print(min_enclosing_rectangle(3,2,9))
#used the count command to calculate the average between yes and no. Abstained isn't important and thus it isn't counted

def vote_percentage(results):
    y=results.count("yes")
    n=results.count("no")
    av=(y/(y+n))
    return(av)


#Put results as the input and called the function but stored the number in variable x. Used if, elif and else statements to create scenario's
def vote():
    results=input("Enter yes, no and abstained votes here:")
    vote_percentage(results)
    x = vote_percentage(results)
    if x == 1.0:
        print("Proposal passes unanimously")
    elif  x < 1.0  and x >=(2/3):
        print("Proposal passes with a super majority")
    elif x < (2/3) and x >= .5:
        print("Proposal passes with simple majority")
    else:
        print("Proposal fails")


#A lot of guess and checking and a couple of pieces of paper gone and I arrived at this equation. Makes sense in hindsight but wasn't so clear at first
#Try as I may I honestly can't see another way of doing this.
def _121o(w):
    l=int(w)
    o=16*w-l*16
    return(l,o)



