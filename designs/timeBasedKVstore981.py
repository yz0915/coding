# Leetcode 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        entries = self.store[key]
        low, high = 0, len(entries) - 1
        res = ""
        while low <= high:
            mid = low + (high - low) // 2
            if entries[mid][1] == timestamp:
                return entries[mid][0]
            elif entries[mid][1] < timestamp:
                res = entries[mid][0]  # Potential result
                low = mid + 1          # Search right half
            else:
                high = mid - 1

        return res