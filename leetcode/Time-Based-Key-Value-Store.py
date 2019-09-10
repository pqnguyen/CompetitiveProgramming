from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        a = self.store[key]
        idx = self.binary_search(a, timestamp)
        if idx == -1:
            return ""
        return a[idx][0]

    def binary_search(self, a, target):
        if len(a) == 0: return -1

        res = -1
        first, last = 0, len(a) - 1
        while first <= last:
            mid = (first + last) // 2
            if a[mid][1] <= target:
                res = mid
                first = mid + 1
            else:
                last = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.set("foo", "foo", 2)
timeMap.set("foo", "too", 4)
print(timeMap.get("foo", 0))
