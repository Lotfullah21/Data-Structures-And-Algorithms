def square(x):
    """_summary_

    Args:
        x (int): an integer value 

    Returns:
        int : square of a numberff
    """
    return x**2

def sqrt(x: int) -> int:
    """
    
    root square of a number
    :param x: an integer 
    :type x: an integer
    :raise TypeError: if x is not an integer
    :return: square root of a number.
     
    """
    return x**0.5

square_list = []
def applyToEach(List: int,fn) -> list:
    for i in range(len(List)):
        List[i] = fn(List[i])
    return List
   
    
applied = applyToEach([1,2,3,4,10],square)
print(applied)