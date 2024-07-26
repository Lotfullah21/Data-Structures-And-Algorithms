def main():
    d = list(map(int, input().split()))
    array = list(map(int, input().split()))
    query = list(map(int, input().split()))
    frequency = freq(query, array)
    for num in frequency.values():
        print(num)
    
    
def freq(q, arr):
    my_dict = {}
    
    for ele in q:
        count = 0
        for item in arr:
            if ele == item:
                count = count + 1
        my_dict[ele] = count
    return my_dict
    
            
    

    
if __name__ == "__main__":
    main()