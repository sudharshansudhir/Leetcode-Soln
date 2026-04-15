class RecentCounter:

    def __init__(self):
        self.queue=[]
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        start=t-3000
        end=t
        if start<=0:
            return len(self.queue)
        i=0
        while i<len(self.queue):
            if self.queue[i]<start or self.queue[i]>end:
                self.queue.pop(i)
            else:
                i+=1
        return len(self.queue)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
