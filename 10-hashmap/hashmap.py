def get_hash_value(key):
    """
    Args:
        key (str): a sequence of characters.

    Returns:
        ASCII: ASCII representation of the key
        hashmap_value: a hashmap value of the input.
    """
    # initialize ASCII value as zero
    init_val = 0
    # look for every char in string
    for ele in key:
        # add the ASCII value of each element to init_val
        init_val = init_val + ord(ele)
    # calculate the hashmap value using ASCII.
    hashmap_value = init_val%100
    
    return ("ASCII value",init_val, "hashmap value",hashmap_value)

get_hash_value("hello")
print(get_hash_value("Hash"))
print(get_hash_value("Hello"))
print(get_hash_value("Good"))