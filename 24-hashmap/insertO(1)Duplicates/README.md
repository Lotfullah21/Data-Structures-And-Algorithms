## Insert Delete GetRandom O(1) - Duplicates allowed

RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.

<h2><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/">leetcode-381</a></h2>

# Algorithm:

Use a list, dictionary (hashmap) and a local set.
`list`: It is used to give us the random element from the data structure, hashmap does not support, even if do so, lots works needs to be done to get some value in specific range at constant time, we might stuck in an infinite loop.
`Dictionary`: It is used, because it is an extremely efficient algorithm for insertion and looking up for a number, basically insertion and removal easily can be done by this data structure.
`Set`: Dictionary does not allow duplicate elements, sets can be used to save the index of an element that occurs multiple times.
So, here how is the relationship between set and dictionary.

```plaintext
{
    value1: set(idx1, idx2, idx3),
    value2: set(idx7, idx8, idx5),
    value3: set(idx9, idx6, idx11)
}
```

## Insertion:

### Algorithm

- Check if value is present, if present, it means there is a value same as the value we want to insert and has a set assigned to it.
  - Assign to the set variable the value of the value we want insert from dictionary.
  - Make the flag variable False
- If value is not present:
  - Create a new set and assign to set variable.
  - Make the flag variable True
- Get the size of the list, this is how we are getting the index.
- Add the index to the set variable
- Add the set as value to in the dictionary corresponding to the number we want to create.
- Add the value at the end of the list
- return Flag.

## Removal

- Check if the value is present, if not:
  - Return False immediately
- If element is present in the dictionary:
  - Get the set corresponding to the element from dictionary
  - set supports pop operation and returns the last elements value removed, use it and save that index.
  - After deleting one index from the set, assign the update set to corresponding value
  - Check if that index is the index of last item in the list, if So:
    - Simply use pop operation in nums list.
  - To avoid more time complexity, simply the index we got using dictionary swap with last elements index.
    - get the last index from the list
    - Save its value
    - Swap the index we got from the set with the last elements index from the nums list
    - Remove the last element from the list using pop operation
    - Now, because the last element was saved somewhere in the dictionary, find it and update its index with the index we got from the set
    - Remove its previous index which was the last index
    - Update it with the removed index we got from the set
    - Update the set corresponding to the value
- At last, check if still there is any index corresponding to a value, if the set is empty, it means there is no occurrence of that number, delete it from dictionary.

## Analysis:

`Time complexity`: O(1)

`Space complexity`: O(N)
