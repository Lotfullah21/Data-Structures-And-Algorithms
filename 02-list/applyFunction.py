def square(x):
    return x**2

def sqrt(x):
    return x**0.5

square_list = []
def applyToEach(List,fn):
    for i in range(len(List)):
        List[i] = fn(List[i])
    return List
   
    
applied = applyToEach([1,2,3,4,10],square)
print(applied)