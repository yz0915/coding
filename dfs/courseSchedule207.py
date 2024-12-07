# lc 207
# https://leetcode.com/problems/course-schedule/

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


def canFinish(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visiting = set()

    def dfs(crs):
        # BASE CASE!!
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True