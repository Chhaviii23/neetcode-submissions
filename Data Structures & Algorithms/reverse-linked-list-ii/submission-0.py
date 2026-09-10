# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes=[]
        curr=head

        while curr:
            nodes.append(curr)
            curr=curr.next
        i = left-1
        j = right-1

        while i<j:
            nodes[i].val,nodes[j].val = nodes[j].val,nodes[i].val
            i +=1
            j -=1
        return head