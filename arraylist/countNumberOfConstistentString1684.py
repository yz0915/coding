# lc 1684
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)

    def check_chars(allowed_set, word):
        for char in word:
            if char not in allowed_set:
                return False
        return True

    res = [word for word in words if check_chars(allowed_set, word)]
    return len(res)