class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = double = head

        while double and double.next:
            single = single.next
            double = double.next.next
            if single == double:
                return True
        return False