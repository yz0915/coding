# leetcode 1323
# https://leetcode.com/problems/maximum-69-number/

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

def maximum69Number (num):
    num_str = str(num)
    char_list = list(num_str)
    
    for i in range(len(char_list)):
        if char_list[i] == '6':
            char_list[i] = '9'
            return int("".join(char_list))
    
    return num