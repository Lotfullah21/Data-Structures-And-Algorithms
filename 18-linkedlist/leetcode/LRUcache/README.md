## LRU Cache

Design a data data that works like a LRU cache, it has a fixed capacity and two methods:

- `get(key)`: It returns the value of the key from LRU cache if present, if not present return -1.
- `put(key, value)`: update the value of key with given value if key is already present, else add the new key-value to the LRU cache. If the capacity of the LRU cache is full, delete the least used item before adding key-value to cache.

<h3><a href="https://leetcode.com/problems/lru-cache/">146. LRU Cache</a></h3>

## Idea:

Just think of your phone, every time you open a new app it does not necessary go through all steps and open the app from scratch.
If an app is already opened, it just uses that.
If an app is not opened, it will open it from scratch and assigns more resources to it.
Now, lets say can have only four opened apps in our cache and the maximum capacity of the cache is four, hence unless we delete one of the apps, this app cannot be opened; Which one to delete? The first opened app or the least used one. Because when an app is not used recently, it will move down into our cache and the one used recently will be on top of the cache.

We need to keep in mind two things.

#### First:

We should have a place to save our items(apps) and the delete, insertion and addition should be at constant time.

#### Second:

We should keep the order to know which item is in use, which item is at the bottom of the cache.

## Solution:

For the firs problem, we have hashmap(dictionary) which all of the operation can be done at constant time, but here we cannot keep the order. To keep the order we use a doubly linked list where addition always happens before the tail.

## Node deletion and addition implementation:

Create two methods, one to delete an item(Node) from any where except head and tail, This method will be used in two scenarios:

1. `deleteNode()`:

- When the LRU cache is full and we need to delete the least used node (after head node).
- When an opened app is used again, we need to delete from the linked list and put in head of LRU cache.

2. `addNode()`:
   The second one is to insert a node(item) just before the tail, it used when open a new app or an old app to add them at the top of the cache.

Head node, tail node and the node to be inserted or deleted will be given by the user.

## Use a dictionary to save the nodes.
