# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

# deeedbbcccbdaa k = 3 => aa

def removeDuplicates(s, k):
    stack = []  # [char, count]

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])

        if stack[-1][1] == k:
            stack.pop()

    res = ""
    for char, count in stack:
        res += char * count

    return res