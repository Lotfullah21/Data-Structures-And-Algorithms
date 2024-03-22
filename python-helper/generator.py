def main():
    n = int(input("How many times you want to see the person laugh: "))
    laughBox = laugh(n)
    for happyFace in laughBox:
        print(happyFace)
    
    
# if the inputs gets bigger and bigger, our computer memory would not able to handle it, because the laugh function returns all the outputs at once.
def laugh(n):
    for i in range(n):
        # it says return little piece of data at a time, not all at once.
        yield "😂"*i

if __name__ == "__main__":
    main()
    