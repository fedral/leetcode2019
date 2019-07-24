# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1,nums2=[1,2,2,1],[2,2]
    nums1.sort() 
    nums2.sort()
    s1,s2=len(nums1),len(nums2)

    if(s1==0 | s2==0):
        return []
    result=[]
    ia,ib = 0,0
    while( ia<s1 and ib<s2):
        if( nums1[ia] == nums2[ib]):
            result.append(nums1[ia])
            ia=ia+1
            ib=ib+1
        elif(nums1[ia] < nums2[ib]):
            ia=ia+1
        else:
            ib=ib+1
         
    return result

print(intersect([1,2,2,1],[2,2]))




def permute(nums):
    if len(nums) <= 1:
        return [nums]
    out = []
    perms = permute(nums[1:])
    for perm in perms:
        for i in range(0, len(perm)+1):
            p = perm[:i] + [nums[0]] + perm[i:]
            out.append(p)
    return out


def cnk(n,k):
    if n==2 and k==2 :
        return 1
    if k==1 :
        return n
    return cnk(n-1,k)+cnk(n-1,k-1)






def quick_sort(array, l, r):
    if(l<r):
        p = partion(array,l,r)
        quick_sort(array,l,p-1)
        quick_sort(array,p+1,r)
        
def partion(array,l,r):
    key = array[l]
    while l < r:
        while l<r and key<=array[r]:
            r-=1
        array[l],array[r] = array[r],array[l] 
        while l<r and key>array[l]:
            l+=1
        array[l],array[r] = array[r],array[l]
    return l

'''


def solution3(s):        
    st = {} 
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans  

print(solution3('abcaccd'))












































