import random
# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 5
# Year: 2021

#helper function 1
'''
str -> list
file must have a lenth greater than 0 and have spaces between them
'''
def users(file):
    '''
    (str)->list of users
    precondition:
    none
    '''
    users=[]
    for i in range(len(file)):
        compare = file[i]
        compare = compare.split()
        if (compare[0] in users) == False:
            users.append(compare[0])
    for i in range(len(file)):
        compare = file[i]
        compare =compare.split()
        if (compare[1] in users) == False:
            users.append(compare[1])
    users = sorted(users)
    return(users)
#helper function 2
def clean_up(list1,list2):
    '''
    2 lists of str -> 1 list of strings'
    preconditions:
    list1 and list 2 must have a lenth greater than 1
    details: takes the rest of the function and fixes it
    '''
    fixed_list=[]
    for i in range(len(list2)):
        compare1 = list2[i]
        friends=[]
        friendo=[]
        friendo.append(compare1)
        for i in range(len(list1)):
            compare2 = list1[i]
            compare2 = compare2.split()
            if compare1 == int(compare2[1]):
                friends.append(int(compare2[0]))
        friendo.append(friends)
        fixed_list.append(tuple(friendo))
        
    return(fixed_list)
        
#helper function 3
'''
list -> sortedlist
preconditions:
list must be a list
'''
def fix_sorting(list):
    sorted_list=[]
    sorted_list2=[]
    for i in range(len(list)):
        sorted_list.append(int((list)[i]))
    sorted_list = sorted(sorted_list)
    for i in range(len(sorted_list)):
        sorted_list2.append(sorted_list[i])
    return(sorted_list2)

#helper function 4
'''
1(2d) list and 1 normal list -> 2d list
preconditons:
network and sorted list must have their conditions fufilled. One being a 2d list and one being a normal list
'''
def fix_sortingnet(network,sortedlist):
    newnet = []
    for i in range(len(sortedlist)):
        compare1= sortedlist[i]
        for i in range(len(network)):
            if compare1 == network[i][0]:
                newnet.append(network[i])
    return(newnet)


    


def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    
    friends = open(file_name).read().splitlines()
    

    # YOUR CODE GOES HERE
    friends.pop(0)
    network=[]
    userslist=users(friends)
    sortedusers = fix_sorting(userslist)
    friendo=[]
    check = 0
    for i in range(len(friends)):            
        compare1 = friends[i]
        compare1 = compare1.split()
        friendlist=[]
        if compare1[0] in userslist:
            friendo.append(int(compare1[0]))
            userslist.remove(compare1[0])
            for h in range(len(friends)):
                compare2=friends[h]
                compare2= compare2.split()
                if compare1[0] == compare2[1] and (compare2[0] in friendlist)== False:
                    friendlist.append(int(compare2[0]))
                elif compare1[0] == compare2[0] and (compare2[1] in friendlist) == False:
                    friendlist.append(int(compare2[1]))
            if len(friendo) > 0:
                friendo.append(friendlist)
                network.append(tuple(friendo))
                friendo=[]
        
    if len(userslist) > 0:
        userslist=fix_sorting(userslist)
        fixed_list=clean_up(friends,userslist)
        for i in range(len(fixed_list)):
            network.append(fixed_list[i])
    network = fix_sortingnet(network,sortedusers)
    network=sorted(network)
    return network
net1 = create_network("net1.txt")
net2 = create_network("net2.txt")
net3 = create_network("net3.txt")
net4 = create_network("big.txt")
net5 = create_network("huge.txt")
def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    
    # YOUR CODE GOES HERE

    a=0
    b=len(network)
    relevant = []
    i=b//2
    while network[i][0] != user1:
        if network[i][0] > user1:
            b=i
            i=b//2
        elif network[i][0] < user1:
            a=i
            i=(b+a)//2
    relevant.append(network[i])   
    a=0
    b=len(network)
    i=b//2
    while network[i][0] != user2:
        if network[i][0] > user2:
            b=i
            i=b//2
        elif network[i][0] < user2:
            a=i
            i=(b+a)//2
    relevant.append(network[i])
    if len(relevant[0][1]) <  len(relevant[1][1]):
        smaller = relevant[0][1]
        larger = relevant[1][1]
    else:
        smaller = relevant[1][1]
        larger = relevant[0][1] 
    for i in range(len(smaller)):
        if (smaller[i] in larger) == True:
            common.append(smaller[i])
    return common


def recommend(user, network): 
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    viable_candidates=[]
    for i in range(len(network)):
        if (user in network[i][1]) == False:
            viable_candidates.append(network[i])
            if user == network[i][0]:
                comparison = network[i]
                viable_candidates.remove(network[i])

    listofcandidates=[]
    for i in range(len(viable_candidates)):
        listofcandidates.append(viable_candidates[i][0])
    common=[]
    for i in range(len(listofcandidates)):
        common.append(len((getCommonFriends(comparison[0],listofcandidates[i],network))))
        
    nice=max(common)
    p=common.index(nice)
    recommend=listofcandidates[p]
    return recommend
   
    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    applicable=0
    for i in range(len(network)):
        if len(network[i][1]) >= k:
            applicable+=1
        
    return applicable


def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    lenths=[]
    for i in range(len(network)):
        lenths.append(len(network[i][1]))
    lenths= max(lenths)
    return lenths

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    
    # YOUR CODE GOES HERE
    lenths=[]
    for i in range(len(network)):
        lenths.append(len(network[i][1]))
    lenths=max(lenths)
    for i in range(len(network)):
        if len(network[i][1]) == lenths:
            max_friends.append(int(network[i][0]))
    return    max_friends

def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''


    # YOUR CODE GOES HERE
    average_no=0
    for i in range(len(network)):
        average_no+=(len(network[i][1]))
    average_no = average_no/(len(network))
    return average_no
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    check = False
    i=0
    while i < (len(network)-1) and check == False:
        if len(network[i][1]) == (len(network)-1):
            check = True
        i+=1

    return check
####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    check = False
    improvlist=[]
    for i in range(len(network)):
        improvlist.append(network[i][0])
    print(improvlist)
    while check == False:
        confirmation=input("Please input a valid ID: ")
        confirmation=confirmation.strip()
        if (int(confirmation) in improvlist) == True:
            check = True
            return(int(confirmation))
        else:
            print("Invalid, please try again")

        


    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")


