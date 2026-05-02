class Solution:
    def rotatedDigits(self, n: int) -> int:
        items=[i for i in range(1,n+1)]
        dict={
            1:1,
            0:0,
            8:8,
            6:9,
            9:6,
            5:2,
            2:5
        }

        c=0
        for i in items:
            i=str(i)
            if "7" in i or "3" in i or "4" in i:
                continue
            rot=""
            for e in i:
                rot+=str(dict[int(e)])
            if rot==i:
                continue

            c+=1

        return c
