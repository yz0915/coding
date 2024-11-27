# lc 134 gas station
# https://leetcode.com/problems/gas-station/

def canCompleteCircuit(gas, cost):
    total_gain = 0
    curr_gain = 0
    answer = 0

    for i in range(len(gas)):
        total_gain += gas[i] - cost[i]
        curr_gain += gas[i] - cost[i]

        # If this becomes negative, it indicates that the journey starting from the current candidate station is not feasible.
        if curr_gain < 0:
            curr_gain = 0
            answer = i + 1

    return answer if total_gain >= 0 else -1