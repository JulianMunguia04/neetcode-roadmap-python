# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next 
            curr.next = prev   
            prev = curr  
            curr = nxt 
        
        return prev
    
# Time complexity: O(n), as we traverse each node once
# Space complexity: O(1), as we only use a few pointers