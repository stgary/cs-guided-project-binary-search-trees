def mergeTwoLinkedLists(l1, l2):
    if not l1:
        return l2
    
    if not l2:
        return l1 
    
    # init two pointers at the start of l1 and l2 
    p1 = l1
    p2 = l2 
    
    # create a new linked list that holds all the values from both linked lists 
    new_list = None 
    # figure out which head value is smaller 
    if p1.value < p2.value:
        new_list = ListNode(p1.value)
        p1 = p1.next
    else:
        new_list = ListNode(p2.value)
        p2 = p2.next 
        
    # keeps track of our location in the new list 
    current = new_list
        
    while p1 and p2:
        if p1.value < p2.value:
            new_node = ListNode(p1.value)
            current.next = new_node 
            current = current.next 
            p1 = p1.next
        else:
            new_node = ListNode(p2.value)
            current.next = new_node 
            current = current.next 
            p2 = p2.next
            
    # at this point, we've finished iterating through one of the linked lists 
    # figure out which list still has nodes 
    if p1: 
        current.next = p1 
    else:
        current.next = p2 
        
    return new_list 
	