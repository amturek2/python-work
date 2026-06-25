class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque
        hp = []
        q = deque()

        for item, count in Counter(tasks).items():
            heapq.heappush(hp, -count)


        time = 0
        res = []
        while len(hp) > 0 or len(q) > 0: 
            time +=1
            if (hp): 
                n_freq = heapq.heappop(hp)
                if (n_freq + 1 != 0): 
                    q.append([n_freq + 1, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(hp, q.popleft()[0])
                   
        return time
 
        