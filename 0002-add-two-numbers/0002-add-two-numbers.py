# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        n1 = l1
        n2 = l2
        i=0
        while(True):
            if(n1==None):
                break
            s += n1.val * (10**i)
            n1 = n1.next
            i+=1
        i=0
        while(True):
            if(n2==None):
                break
            s += n2.val * (10**i)
            n2 = n2.next
            i+=1

        s1 = list(reversed(str(s)))
        head = ListNode()
        curr_node = head

        c = 0

        while(True):
            if(len(s1)<=c):
                break
            new_node = ListNode(int(s1[c]))
            curr_node.next = new_node
            curr_node=curr_node.next
            c+=1

        return head.next