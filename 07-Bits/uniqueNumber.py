def main():
    n = int(input(""))
    arr = list(map(int, input("").split()))
    print(single_num(arr))
    
def single_num(arr):
    ans = 0
    for i in range(len(arr)):
        ans = ans ^ arr[i]
    return ans
    

if __name__ == "__main__":
    main()

