def splitTupe(Tuple):
    # tuple to gather the numbers
    numbers = ()
    # tuple to gather the words
    unique_words = ()
    words = ()
    for t in Tuple:
        # in this tuple (num, word), means t[0] is a number, the latter one is a word.
        numbers = numbers + (t[0],)
        words = words + (t[1],)
        # avoid adding repeated tuples
        if t[1] not in unique_words:
            unique_words = unique_words + (t[1],)
    return numbers, words, unique_words


nums, words, unique = splitTupe((
    (1, "Hello"), (2, "Salam"), (10, "Bonjur"), (0, "Namasti"), (21, "Salam")))
print(nums)
print(words)
print("Unique words", unique)
