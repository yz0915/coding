# Leetcode 40 Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/
# Input: candidates = [10,1,2,7,6,1,5], target = 8 Output: [[1,1,6], [1,2,5], [1,7], [2,6]]

class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return
        if target == 0:
            answer.append(path)
            return
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(candidates, target - candidates[i], i + 1, path + [candidates[i]], answer)