Implement the following data structure:
If you have 1000 keys with values from 0-999, implement search, insertion and deletion in `O(1)` time.

## Idea:

Create an array of size keys and assign to the index of given key value 1.

### Insert(i):

- Add 1 to the index of given key

### Delete(i):

- Search
  - if the given key has value 1 (key==1):
    - Make that index's value to be 0
  - else:
    - return -1

### Search(i):

- Search
  - if the given key has value 1 (key==1):
    - return the index
  - else:
    - return -1

## Analysis:

`Time Complexity`: All of the above operation can be done in `O(1)`.
`Space Complexity`: `O(n)`, where n is size of the bucket.
