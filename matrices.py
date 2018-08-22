from pprint import pprint

'''Represents a single matrix transformation acting on a point'''
class Transform:
	
    def __init__(self, matrix, delta):
        self.matrix = matrix
        self.delta = delta
    
    def evaluate(point):
        newX = mmult([point.x, point.y], matrix[0]) + delta[0]
        newY = mmult([point.x, point.y], matrix[1]) + delta[1]
        return Point(newX, newY)
    
    def mmult(vect1, vect2):
        return sum(z[0]*z[1] for z in zip(vect1,vect2))
        

'''Represents a single point with x/y coordinates'''
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    point1 = Point(1,2)
    point2 = Point(3.5,-1.8)
    transform = Transform([[0,1],[2,3]], [4,5])
    
    print 'Point1: x=%d, y=%d' % (point1.x, point1.y)
    print 'Point2: x=%d, y=%d' % (point2.x, point2.y)
    print '\nTransform:'
    print 'Matrix:'
    pprint(transform.matrix)
    print 'Delta:'
    pprint(transform.delta)
    
    