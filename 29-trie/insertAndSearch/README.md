## Search Query for Strings

Given an array of strings (consisting of lowercase characters) arr[] of size N. Also, you will be given some queries Q and for each query a string is given and your task is to check if the given string is in the string array or not.

<h3><a href="https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/DSASPPY-Trie/problem/search-query-for-strings5049">GFG</a></h3>

# Analysis:

## Trie

### Insertion:

The time complexity is O(L) where L is length of the string, it is because we need to process each character.

### Search:

The time complexity is O(L) where L is length of the string, it is because we need to search for each index.

The Trie guarantees O(L), time complexity regardless of the number of words stored, making it more predictable for search and insert operations, especially with longer keys and potential hash collisions in hash tables.

## Hash map

in a hash table, the average time complexity for both insert and search operations is O(1).
O(1) is due to hashing. However, in the worst-case scenario, where many collisions occur, the time complexity can degrade to O(N), where N is the number of entries in the hash table.
