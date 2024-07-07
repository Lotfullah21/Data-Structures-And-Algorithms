def main():
    ch = input("enter a character: ")
    check_case(ch)
    
def check_case(n):
    if n >="a" and n<="z":
        print("lower case")
    elif n>="A" and n<="Z":
        print("upper case")
    else:
        print("None of the above")
        
if __name__ =="__main__":
    main()