class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # Create two dummy heads for the two partitions
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to track the current ends of the two lists
        smaller_ptr = smaller_head
        greater_ptr = greater_head
        
        current = head
        
        while current:
            if current.val < x:
                smaller_ptr.next = current
                smaller_ptr = smaller_ptr.next
            else:
                greater_ptr.next = current
                greater_ptr = greater_ptr.next
            current = current.next
            
        # Terminate the greater list to avoid cycles
        greater_ptr.next = None
        
        # Connect the smaller list's tail to the greater list's head
        smaller_ptr.next = greater_head.next
        
        return smaller_head.next