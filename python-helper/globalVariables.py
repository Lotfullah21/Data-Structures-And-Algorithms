saving = 0

def main():
    print("saving",saving)
    withdraw(20)
    print("saving after withdrawing",saving)
    deposit(230)
    print("saving after depositing",saving)
    

def withdraw(n):
    global saving
    saving = saving - n

def deposit(n):
    global saving
    saving = saving + n
    

if __name__ == "__main__":
    main()