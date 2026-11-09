# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sen = ListNode()
        head = sen
        temp1 = list1
        temp2 = list2
        while temp1 != None or temp2 != None:
            if temp1 == None:
                save = temp2.next
                sen.next = temp2
                sen = sen.next
                temp2 = save
                print("1")
            elif temp2 == None:
                save = temp1.next
                sen.next = temp1
                sen = sen.next
                temp1 = save
                print("2")
            else:
                if temp1.val <= temp2.val:
                    print(f" val1: {temp1.val} val2: {temp2.val}")
                    save = temp1.next
                    sen.next = temp1
                    sen = sen.next
                    temp1 = save
                else:
                    save = temp2.next
                    sen.next = temp2
                    sen = sen.next
                    temp2 = save
        return head.next
            


