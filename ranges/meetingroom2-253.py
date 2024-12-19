# 253. Meeting Rooms II - count meetings needed
# https://leetcode.com/problems/meeting-rooms-ii/

'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Example 1: Input: [[0, 30],[5, 10],[15, 20]], Output: 2
Example 2: Input: [[7,10],[2,4]]. Output: 1
'''

def minMeetingRooms(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res