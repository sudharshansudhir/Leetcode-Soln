class CustomStack:

    def __init__(self, maxSize: int):
        self.stk=[]
        self.m=maxSize

    def push(self, x: int) -> None:
        if len(self.stk)==self.m:
            return 
        self.stk.append(x)


    def pop(self) -> int:
        if self.stk:
            return self.stk.pop()
        return -1


    def increment(self, k: int, val: int) -> None:
        if k>len(self.stk):
            self.stk=[i+val for i in self.stk]
        else:
            for i in range(k):
                self.stk[i]=self.stk[i]+val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
