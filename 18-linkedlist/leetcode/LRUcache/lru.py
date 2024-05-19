class LRUCache:
    class Node:
        def __init__(self):
            self.key = 0
            self.value = 0
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {}

        

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        else:
            app = self.hm[key].value
            temp = self.deleteNode(self.head,self.hm[key])
            # Re-order the cache
            self.addNode(self.head, self.tail, temp)
            return app

        

    def put(self, key: int, value: int) -> None:
        app = self.hm.get(key)
        if app is None:
            if len(self.hm)==self.capacity:
                del self.hm[self.head.next.key]
                self.deleteNode(self.head, self.head.next)
            # Create a new node
            node = self.Node()
            node.key = key
            node.value = value
            self.hm[key] = node
            self.addNode(self.head, self.tail, node)
        # If the node is already present
        else:
            app.value = value
            self.deleteNode(self.head, app)
            self.addNode(self.head, self.tail ,app)


    def addNode(self, head, tail, node):
        nodePrev = tail.prev
        nodePrev.next = node
        node.next = tail
        node.prev = nodePrev
        tail.prev = node
    
    def deleteNode(self, head, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
       
        node.next = None
        node.prev = None

        return node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)