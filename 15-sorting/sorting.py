class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Sfort method
    def __lt__(self,other):
        # If x values are same, sort based on lower y values.
        if self.x==other.x:
            return self.y<other.y
        else:
            return self.x<other.x

l = [Coordinate(2, 3),Coordinate(1, 12),Coordinate(2, 3),Coordinate(4, 7),Coordinate(1, 5)]

l.sort()

for element in l:
    print(element.x, element.y)
    
