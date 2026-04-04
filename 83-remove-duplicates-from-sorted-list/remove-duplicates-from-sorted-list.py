class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # skip duplicate
                current.next = current.next.next
            else:
                current = current.next
        
        return head