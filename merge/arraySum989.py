# 989. https://leetcode.com/problems/add-to-array-form-of-integer/
# Example 1: Input: num = [1,2,0,0], k = 34 Output: [1,2,3,4] Explanation: 1200 + 34 = 1234

def addToArrayForm(self, num, k):
    ans = []
    i = len(num) - 1
    carry = 0
    while i >= 0 or k > 0 or carry:
        ssum = carry
        if i >= 0:
            ssum += num[i]
        if k > 0:
            ssum += k % 10
        ans.append(ssum % 10)
        carry = ssum // 10
        i -= 1
        k = k // 10
    return ans[::-1]
