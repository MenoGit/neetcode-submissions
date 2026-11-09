# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        dummy = ListNode(0,head)
        while temp is not None:
            length += 1
            temp = temp.next

        print(f"n = {n}")
        print(f"length = {length}")
        
    
        remove = length - n 
        print(f"remove = {remove}")

        offset = dummy
        while remove > 0 and offset is not None:
            offset = offset.next
            remove -= 1

        if offset:
            print(f"offset = {offset.val}")
            if offset.next:
                offset.next = offset.next.next

        return dummy.next 

def print_linked_list(head: ListNode):
    temp = head
    while temp is not None:
        print(f"{temp.val}")
        temp = temp.next

        
        