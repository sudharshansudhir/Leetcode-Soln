class Solution:
    def removeCoveredIntervals(self, iv: List[List[int]]) -> int:
        iv.sort(key=lambda x:(x[0],-x[1]))
        news=[]
        for i in iv:
            if not news:
                news.append(i[:])
            else:
                if i[0]>=news[-1][0] and i[1]<=news[-1][1]:
                    continue
                else:
                    news.append(i[:])
        return len(news)