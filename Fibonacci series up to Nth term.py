mod=pow(10,9)+7
class Solution:
    def series(self, n):
        # Code here
        p=[]
        p.append(0)
        p.append(1)
        for i in range(2,n+1):
            sm=(p[-1]+p[-2])%mod
            p.append(sm)
        return p

  #daily challenge (23/03/2024)
