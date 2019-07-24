class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        if s=="":
            return ""
        l=len(s)
        '''
        对于每个位置，利用中心扩散法 找到最长回文子串，时间复杂度O(N^2)
        '''
        def centerspread(left,right):
            if left>right:
                return 
            else:
                while left>=0 and right<l and s[left]==s[right]:
                    left-=1
                    right+=1
                return s[left+1:right],right-left-1
                    
        res=""
        for i in range(len(s)):
            s1,l1=centerspread(i,i)
            s2,l2=centerspread(i,i+1)
            tmp = s1 if l1>=l2 else s2
            res = res if len(res)>=len(tmp) else tmp
        return res
                
    
'''
执行用时 :696 ms, 在所有 Python 提交中击败了72.31%的用户
内存消耗 :11.9 MB, 在所有 Python 提交中击败了32.27%的用户
'''
             
            
# to-do  马拉车算法  O(N)


        
        
        