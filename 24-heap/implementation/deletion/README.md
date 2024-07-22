## Remove From the Heap

## Approach

1. Swap the 0th index with last index
2. Delete the last index
3. Now our heap property might have been disturbed, start fixing from the top, Multiple Case could be faced.

   - Case-1:
     - `val(i)<=left child` and `val(i)<=right child`, ideal case nothing to fix; Break out of the loop.
   - Case-2:
     - `val(i)<=left child` and `val(i)>right child`, left side is fixed, fix the right side by swapping the right child element with the parent which is at index i.
   - Case-3:
     - `val(i)>left child` and `val(i)<=right child`, right side is fixed, fix the left side by swapping the left and parent index.
   - Case-4:
     - `left child<val(i)>right child`, both sides have problems, pick the min child and swap it with the parent.
   - Case-final:
     - Cases from 2nd to 4th can be categorized into one single case which is the parent is either greater from left or right child, to fix, just pick the child with minimum value and swap it with parent index(i).

## Time Complexity:

Removing from the end of a list takes `O(1)` operations.
`O(logN)`, we are traversing the height of the tree.
