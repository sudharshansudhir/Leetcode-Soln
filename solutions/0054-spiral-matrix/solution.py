class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        s=[]
        row=len(matrix)
        col=len(matrix[0])
        up=True
        seq=True
        i=j=k1=k2=0
        n=len(matrix)*len(matrix[0])
        while n>0:
            print(i,j,s)
            if(up and seq):
                s.append(matrix[i][j])
                j+=1
                if(j==len(matrix[0])-k1):
                    j-=1
                    i+=1
                    k2+=1
                    up=False
                    seq=False
            elif((not up) and (not seq)):
                s.append(matrix[i][j])
                i+=1
                if(i==len(matrix)-k1):
                    i-=1
                    j-=1
                    k1+=1
                    seq=True
                    # up=False
            elif(seq and not up):
                s.append(matrix[i][j])
                j-=1
                if(j==-2+k1):
                    up=True
                    seq=False
                    j+=1
                    # k1+=1
                    i-=1
            elif(not seq and up):
                s.append(matrix[i][j])
                i-=1
                if(i==-1+k2):
                    i+=1
                    # k2+=1
                    j+=1
                    seq=True
                    up=True
            n-=1
        print(s)
        return s

