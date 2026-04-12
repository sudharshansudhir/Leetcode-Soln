class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans=[]
        for i in range(len(words)):
            ii=words[i][::-1]
            if (ii in words[:i] or ii in words[i+1:]) and ii[::-1] not in ans and ii not in ans:
                ans.append(ii)
        print(ans)
        return len(ans)
