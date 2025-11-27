# Last updated: 11/26/2025, 5:40:35 PM
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)    


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.times[key]
        if not values or timestamp < values[0][0]:
            return ""

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] < timestamp:
                result = values[mid][1]
                l = mid + 1
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                return values[mid][1]
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)