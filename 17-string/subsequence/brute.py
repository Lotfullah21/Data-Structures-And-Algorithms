def all_subsequences(s):
    """
    Generate all subsequences of a string using a brute force approach with loops.
    
    :param s: The input string.
    :return: A list of all subsequences of the input string.
    """
    n = len(s)
    subsequences = []

    # Number of subsequences will be 2^n
    for i in range(1, 2**n):
        subsequence = ""
        for j in range(n):
            # Check if j-th bit in i is set
            if (i >> j) & 1:
                subsequence += s[j]
        subsequences.append(subsequence)

    return subsequences

# Test the function
string = "abcd"
print(all_subsequences(string))
