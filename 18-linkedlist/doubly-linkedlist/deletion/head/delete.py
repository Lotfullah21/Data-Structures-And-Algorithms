def deleteHead(head):
    # If head is empty
    if head is None:
        return None
    # If only one is present, after removing, nothing is going to be remained there; return None
    if head.next is None:
        return None
    else:
        temp = head.next
        head = temp
        head.prev = None
        return head