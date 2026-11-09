# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        temp = head.next
        if temp == None:
            return False
        
        while temp.next != None:
            if temp.next == head:
                return True
            temp = temp.next
            temp = temp.next
            if temp == None:
                return False
            head = head.next
        return False
        