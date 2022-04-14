# Family name: Keith Compere
# Student number: 300246636
# Course: IT1 1120
# Assignment number: 6
# Year: 2021

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


#13/13 done
class Rational():
    def __init__(self, numerator=0, denominator=0):
        self.num = numerator
        self.den = denominator

r1 = Rational(3,2)

class Rectangle():
    def __init__(self,bottom_left_corner=Point(), top_right_corner=Point(),color=""):
        self.blc=bottom_left_corner
        self.trc=top_right_corner
        self.color=color

    def __eq__(self,other):
        '''(rectangle,rectangle)->bool
        Returns True if self and other have the same coordinates'''
        return(self.blc==other.blc and self.trc==other.trc)
    
    def __repr__(self):
        '''(rectangle)->str
        Returns canonical string representation of rectangle'''  
        return('Rectangle(Point('+str(self.blc.x)+','+str(self.blc.y)+')'+','+'Point('+str(self.trc.x)+','+str(self.trc.y)+')'+','+"'"+self.color+"'"+')')

    def __str__(self):
        '''(rectangle)->str
        Returns nice string representation of rectangle.
        '''
        return("I am a "+self.color+' '+ "rectangle with a bottom left corner at "+'('+str(self.blc.x)+','+str(self.blc.y)+')'+' '+"and a top right corner at "+'('+str(self.trc.x)+','+str(self.trc.y)+')')       
    def get_bottom_left(self):
        '''
        rectangle -> Point
        '''
        return(self.blc)
    
    def get_top_right(self):
        '''
        rectangle -> Point
        '''
        return(self.trc)
    
    def get_color(self):
        '''
        rectangle -> str
        '''
        return(self.color)
    
    def reset_color(self,color):
        '''
        (rectangle,str)->none
        '''
        self.color=color
    
    def get_perimeter(self):
        '''
        rectangle->int/flt
        '''
        first_side=(self.trc.y-self.blc.y)
        second_side=(self.trc.x-self.blc.x)
        return((first_side*2)+(second_side*2))
    
    def get_area(self):
        '''
        Rectangle -> int/flt
        '''
        first_side=(self.trc.y-self.blc.y)
        second_side=(self.trc.x-self.blc.x)
        return(first_side*second_side)       
    
    def move(self,xmove,ymove):
        '''
        rectangle -> none
        '''
        self.blc.y=self.blc.y.__add__(ymove)
        self.blc.x=self.blc.x.__add__(xmove)
        self.trc.y=self.trc.y.__add__(ymove)
        self.trc.x=self.trc.x.__add__(xmove)
    
    def intersects(self,rectangle): #check later pretty sure this is wrong.
        '''
        (rectangle,rectangle) -> bool
        '''
        if ((self.trc.x >= rectangle.blc.x) and (self.trc.x <= rectangle.trc.x)) or((rectangle.blc.x >= self.blc.x) and (rectangle.trc.x <= self.trc.x)) :
            if (self.trc.y <= rectangle.trc.y and self.trc.y >= rectangle.blc.y) or ((rectangle.trc.y <= self.trc.y) and (rectangle.trc.y >= self.blc.y)):
                return(True)
            else:
                return(False)
        else:
            return(False)
    
    def contains(self,x,y):
        '''
        (rectangle,2(int/flt)) -> bool
        '''
        if (self.blc.x <= x and self.trc.x >= x) and (self.trc.y >= y and y >= self.blc.y):
            return(True)
        else:
            return(False)


#5/8 done
class Canvas(list):
    
    def add_one_rectangle(self,rectangle):
        '''
        (list,rectangle) -> none
        '''
        self.append(rectangle)
    
    def count_same_color(self,color):
        '''
        (list,str) -> int
        '''
        match=0
        for i in range(len(self)):
            if self[i].color == color:
                match+=1
        return(match)
    
    def total_perimeter(self):
        '''
        (list) -> int/flt
        takes in the list of rectangles and returns an integer or float value based on their total perimeter
        '''
        perimeter=0
        for i in range(len(self)):
            perimeter+=self[i].get_perimeter()
        return(perimeter)
    
    def min_enclosing_rectangle(self):
        '''
        (list) -> rectangle
        takes in the list of rectangles to form a rectangle that the smallest rectangle to enclose all of them.
        '''
        min_x_blc=[]
        min_y_blc=[]
        for i in range(len(self)):
            min_x_blc.append(self[i].blc.x)
            min_y_blc.append(self[i].blc.y)
        min_x=min(min_x_blc)
        min_y=min(min_y_blc)

        max_x_trc=[]
        max_y_trc=[]
        for i in range(len(self)):
            max_x_trc.append(self[i].trc.x)
            max_y_trc.append(self[i].trc.y)  
        max_x=max(max_x_trc) 
        max_y=max(max_y_trc)

        return(Rectangle(Point(min_x,min_y),Point(max_x,max_y),"green"))



    def common_point(self): 
        '''
        (list) -> bool
        '''
        i=0
        check = True
        '''
        checklist=[]
        for i in range(len(self)):
            h=i
            for i in range(len(self)):
                
                checklist.append((self[h]).intersects(self[i]))
        print(checklist)
        if (False in checklist) == True:
            return(False)
        elif (False not in checklist)==True:
            return(True)
        '''
        if ((self[0].intersects(self[1])) == True) and ((self[2].intersects(self[3]))==True) and ((self[1].intersects(self[2]))==True) and (self[0].intersects(self[3])==True):
            return(True)
        else:
            return(False)



