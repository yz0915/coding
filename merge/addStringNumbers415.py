# 415. Add two Strings numbers
# https://leetcode.com/problems/add-strings/

def addStrings(num1, num2):
    ans = []
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(num1[i])
        if j >= 0:
            carry += int(num2[j])
        ans.append(str(carry % 10))
        carry //= 10
        i -= 1
        j -= 1

    return ''.join(ans[::-1])