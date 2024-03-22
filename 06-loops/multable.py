def main():
    n = int(input("Enter a number "))
    range_table = int(input("Enter the range which table is going to be generated: "))
    table(n,range_table)
    
def table(n: int,range_table: int) -> str:
    """generate a table which is multiple of the input n.

    Args:
        n (int): a number that table is going to be generated.

    Returns:
        str: a table
    """
    for i in range(range_table):
        print(i+1,"*",n,"=",(i+1)*n)

    
if __name__ == "__main__":
    main()