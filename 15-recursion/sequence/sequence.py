def fun1(n: int) -> list[int]:
    "Uses recursion to print a sequence"
    if n<1:
        return 
    else:
        print(n)
        fun1(n-1)
        print(n)
        
        
# Example usage    
fun1(4)