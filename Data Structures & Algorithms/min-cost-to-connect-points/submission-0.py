class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj={i:[] for i in range(n)}

        for i in range(n):
            x1,y1 =points[i]
            for j in range(i+1,n):
                x2,y2=points[j]

                dist=abs(x2-x1)+abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        # prims
        res=0
        visit=set()
        minh=[[0,0]] #[cost,point]
        while len(visit)<n:
            cost,i=heapq.heappop(minh)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for neicost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minh,[neicost,nei])
        return res
        