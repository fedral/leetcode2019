class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        a=[0]*len(T)
        
        for i in range(len(T)-2,-1,-1):
            if T[i]<T[i+1]:
                a[i]=1
            else:
                k=i+1
                while True:
                    if T[i]<T[k]:
                        a[i]=k-i
                        break
                    if a[k]==0:
                        a[i]=0
                        break
                    k+=a[k]
        return a
                
                
                