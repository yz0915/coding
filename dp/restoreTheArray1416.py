# https://leetcode.com/problems/restore-the-array/

# Input: s = "1317", k = 2000
# Output: 8
# Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

# let dfs(x) = dp[x] be the number of arrays for the suffix substring s[x ~ m - 1]

#                                            dp[0]: 1317
#                      /                        |           \                  \ 
#           dp[1]:1+317                   dp[2]:13+17       dp[3]:131+7       dp[4]:1317+""
#                /      |       \
#     dp[1]:3+17    dp[2]:31+7   dp[3]:317+""

def numberOfArrays(self, s: str, k: int) -> int:
    m, n = len(s), len(str(k))
    mod = 10 ** 9 + 7   
    dp = [0] * (m + 1)
    
    # Number of possible splits for s[start ~ m-1].
    def dfs(start):
        # If we have already updated dp[start], return it.
        if dp[start]:
            return dp[start]
        
        # There is only 1 split for an empty string.
        if start == m:
            return 1
        
        # Number can't have leading zeros.
        if s[start] == '0':
            return 0
        
        # For all possible starting number, add the number of arrays 
        # that can be printed as the remaining string to count.
        count = 0
        for end in range(start, m):
            curr_number = s[start: end + 1]
            if int(curr_number) > k:
                break
            count += dfs(end + 1)
            
        # Update dp[start] so we don't recalculate it later.
        dp[start] = count % mod
        return count
    
    return dfs(0) % mod