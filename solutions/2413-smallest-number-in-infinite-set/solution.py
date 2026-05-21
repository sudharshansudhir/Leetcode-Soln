class SmallestInfiniteSet:
    def __init__(self):
        self.arr=[i for i in range(1,1001)]

    def popSmallest(self) -> int:
        p=min(self.arr)
        self.arr.remove(p)
        return p
        

    def addBack(self, num: int) -> None:
        if num not in self.arr:
            self.arr.insert(0,num)
        # self.ptr+=1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
