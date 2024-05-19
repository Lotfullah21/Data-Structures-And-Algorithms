### 138. Copy List with Random Pointer

<h3><a href="https://leetcode.com/problems/copy-list-with-random-pointer/description/">leetcode-138</a></h3>

Input: Linked list with their random pointers.

```rust

Node 1: val = 1, next -> Node 2, random -> Node 3
Node 2: val = 2, next -> Node 3, random -> Node 1
Node 3: val = 3, next -> None, random -> Node 2

```

```plaintext

1 --> 2 --> 3 --> None
|     |     |
v     v     v
3     1     2

```
