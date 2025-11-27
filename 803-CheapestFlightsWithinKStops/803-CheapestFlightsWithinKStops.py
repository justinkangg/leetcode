# Last updated: 11/26/2025, 5:40:42 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))

        q = deque([src])
        stops = -1
        while q and stops < k:
            temp_prices = prices.copy()
            for _ in range(len(q)):
                src = q.popleft()
                for nxt, d in adj[src]:
                    if temp_prices[nxt] > prices[src] + d:
                        temp_prices[nxt] = prices[src] + d
                        q.append(nxt)
            prices = temp_prices
            stops += 1

        return -1 if prices[dst] == float('inf') else prices[dst]
        