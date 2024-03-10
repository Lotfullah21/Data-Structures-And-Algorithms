class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self,other):
        if self.x==other.x:
            return self.y<other.y
        else:
            return self.x<other.x
        
l = [Coordinate(2, 3),Coordinate(1, 12),Coordinate(2, 3),Coordinate(4, 7),Coordinate(1, 5)]

l.sort()

for i in l:
    print(i.x, i.y)



t = (1, 4, 5, 6, 7, 0, 2, 3)
new_tuple= sorted(t)
print(new_tuple, type(new_tuple))


# Sorts based on each single character.
s = "leetcode"
new_s = sorted(s)
print(new_s, type(new_s))


d = {1:"gfg",2:"leetcode",3:"hoshmandlab"}
# Sorts based on the keys.
new_dict = sorted(d)
print(new_dict, type(new_dict))