'''Represents a single matrix transformation acting on a point'''
class Transform:
	
    def __init__(self, matrix, delta):
        self.matrix = matrix
        self.delta = delta
    
    