def main():
    ch = input("enter a character: ")
    check_case(ch)
    
def check_case(n):
    if n >="a" and n<="z":
        print("lower case")
    else:
        print("upper case")
        
if __name__ =="__main__":
    main()