# Insertion

Insertion is done in `O(logN)`, because we are traveling height of the tree and swapping the elements.

# How it works

```text
[]
10
```

```text
[10]
```

```text

Insert 5
Append 5 to the array.
Compare with parent (10):
5 < 10, so swap 5 and 10.

  5
 /
10

[5, 10]

```

```text

Insert 20
Append 20 to the array.
Compare with parent (5):
20 > 5, so no swap needed.

  5
 / \
10  20

[5, 10, 20]

```

```text

Insert 2
Append 2 to the array.
Compare with parent (10):
2 < 10, so swap 2 and 10.
Compare with new parent (5):
2 < 5, so swap 2 and 5.

    2
   / \
  5  20
 /
10

[2, 5, 20, 10]




```

```text


```

```text


```

```text


```
