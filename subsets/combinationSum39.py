from typing import List

# 39. Combination Sum - medium
# Input: candidates = [2,3,6,7], target = 7 Output: [[2,2,3],[7]]
# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)

        return results
    
sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target))