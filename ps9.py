# 6.00 Problem Set 9
#
# Name: Hari John Kuriakose
# Collaborators: Hari John Kuriakose
# Time: 5:36 PM, Mon Sep 6, 2010

from string import *
import re

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: base of the triangle
        height: height of perpendicular to the base
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns approximate area of the triangle
        """
        return 0.5*(self.base*self.height)
    def __str__(self):
        return 'Triangle with base ' + str(self.base) +\
               ' and height ' + str(self.height)  
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and height.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base\
        and self.height == other.height


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shape_list = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        for i in self.shape_list:
            if i == sh: 
                print 'Identical shapes !!!' 
                return
        print 'Adding shape to the set ...'
        self.shape_list.append(sh) 
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return self 
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        for i in self.shape_list:
            if isinstance(i, Circle): print i.__str__()
        for i in self.shape_list:
            if isinstance(i, Square): print i.__str__()
        for i in self.shape_list:
            if isinstance(i, Triangle): print i.__str__()

        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    temp, max = 0.0, 0.0
    largest_list = []
 
    for i in shapes.shape_list:
        temp = i.area()
        if temp > max: max = temp
    for i in shapes.shape_list:
        temp = i.area()
        if temp == max: largest_list.append(i)

    print largest_list


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    f = open(filename, 'r')
    text = re.findall('(\w+),(\S+)', f.read())

    for i in text: 
        if i[0] == 'square': 
            obj = Square(i[1])
            shape_set.addShape(obj)
        elif i[0] == 'circle':
            obj = Circle(i[1])
            shape_set.addShape(obj)
        elif i[0] == 'triangle':
            l = i[1].find(',')
            obj = Triangle(float(i[1][:l]), float(i[1][l + 1:]))
            shape_set.addShape(obj)
    
    shape_set.__str__()


