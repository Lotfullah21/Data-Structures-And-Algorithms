def deleteTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    # Find the 2nd last node and make its next to point to None.
    while curr.next.next!=None:
        curr = curr.next
    curr.next = None
    return head