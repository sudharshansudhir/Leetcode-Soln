class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        s=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and queryTime<=endTime[i]:
                s+=1
        return s
