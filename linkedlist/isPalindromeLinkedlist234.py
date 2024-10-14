# isPalindrome solves Leetcode 234 - easy
# https://leetcode.com/problems/palindrome-linked-list/
# N: 1 -> 2 -> 3 -> 2 -> 1 (odd)
# F: f0        f1        f2
# S: s0   s1   s2   s3(need to here) =>  if fast != nil, slow=slow.next
# N: 1 -> 2 -> 3 -> 3 -> 2 -> 1 -->nil (even)
# F: f0        f1       f2         f3
# S: s0   s1   s2  s3(stop)

class Solution:
    def isPalindrome(self, head):
        stack = []
        fast = head
        slow = head
        #finding the middle element
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True