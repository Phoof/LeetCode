# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head.next is not None:
            lst.append(head.val)
            head = head.next
        lst.append(head.val)
        for i in range(1 + len(lst) // 2):
            if lst[i] != lst[-i - 1]:
                return False
        return True