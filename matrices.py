from pprint import pprint
from graphics import Point

'''Represents a single matrix transformation acting on a point'''
class Transform:
	
    def __init__(self, matrix, delta):
        self.matrix = matrix
        self.delta = delta
    
    def transform(self, point):
        newX = self.mmult([point.x, point.y], self.matrix[0]) + self.delta[0]
        newY = self.mmult([point.x, point.y], self.matrix[1]) + self.delta[1]
        return Point(newX, newY)
    
    def mmult(self, vect1, vect2):
        return sum(z[0]*z[1] for z in zip(vect1,vect2))


if __name__ == '__main__':
    point1 = Point(1,2)
    point2 = Point(3.5,-1.8)
    transform = Transform([[0,1],[2,3]], [4,5])
    
    print 'Point1: x=%f, y=%f' % (point1.x, point1.y)
    print 'Point2: x=%f, y=%f' % (point2.x, point2.y)
    print '\nTransform:'
    print 'Matrix:'
    pprint(transform.matrix)
    print 'Delta:'
    pprint(transform.delta)
    
    