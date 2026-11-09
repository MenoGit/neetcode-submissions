# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
    
        half = head
        #if length % 2 != 0:
        #    length += 1
        for i in range(int(length/2)):
            half = half.next

        tail = self.reverse(half)

        temp = head

        while head is not None and tail is not None:
            if head == tail:
                head.next = None
                break

            elif head.next == tail:
                head.next = tail
                head = head.next
                head.next = None
                break
            else:
                prev = head.next
                head.next = tail
                tail = tail.next
                head = head.next
                head.next = prev
                head = head.next

        
    def reverse(self, node):
        head = node
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev 
