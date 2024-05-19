# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        temp = head
        # Important edge case
        if head is None:
            return None
        
        # Step 1: Create new nodes and insert them after each original node
        while temp is not None:
            new_node = Node(temp.val)
            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node
            temp = next_node
        
        # Step 2: Copy the random pointers
        temp = head
        while temp is not None:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Step 3: Separate the new nodes to form the copied list
        temp = head
        new_head = head.next if head else None
        while temp is not None:
            new_node = temp.next
            temp.next = new_node.next
            temp = temp.next
            if new_node.next:
                new_node.next = new_node.next.next
        
        return new_head

# Helper function to print the list
def print_list(head):
    nodes = []
    randoms = []
    while head is not None:
        nodes.append(head.val)
        randoms.append(head.random.val if head.random else None)
        head = head.next
    print("Nodes: ", nodes)
    print("Randoms: ", randoms)

# Example usage
if __name__ == "__main__":
    # Construct the list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node1
    node3.random = node2

    # Copy the list
    solution = Solution()
    copied_list = solution.copyRandomList(node1)

    # Print the original and copied lists
    print("Original list:")
    print_list(node1)
    print("Copied list:")
    print_list(copied_list)
