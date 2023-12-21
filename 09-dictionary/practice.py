def main():
    n,m = (int, input("").split())
    arr = list(map(int, input("").split()))
    query = list(map(int, input("").split()))
    arr_dict = freq(arr)
    print(arr_dict)
    count_of_ele = most_common(arr_dict, query)
    for count in count_of_ele:
        print(count)
    print(count_of_ele)
    


def freq(arr):
    my_dict = {}
    for ele in arr:
        if ele in my_dict:
            my_dict[ele] = my_dict[ele] + 1
        else:
            my_dict[ele] = 1
            
    return my_dict

def most_common(dict_arr, queries):
    count_values = []
    for ele in queries:
        if ele in dict_arr:
            count_values.append(dict_arr[ele])
    return count_values
        
if __name__ == "__main__":
    main()