# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hashmap = {}
        temp = head
        i = 0
        while temp is not None:
            hashmap[i] = temp
            temp = temp.next
            i += 1

        length = len(hashmap)
        i = 1
        check = False
        for j in range(length-1):
            if check == True:
                head.next = hashmap[i]
                head = head.next
                i+=1
                check = False
            else:
                head.next = hashmap[length - i]
                head = head.next
                check = True
        head.next = None

                


            


