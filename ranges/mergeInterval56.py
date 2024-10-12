# mergeInterval - medium
# Time: O(nlogn), space: O(n)

class Solution:
    def merge(self, intervals):
        # sort方法 O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output