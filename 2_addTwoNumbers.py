# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=ListNode(-1) #dummy node
        p1,p2,p3=l1,l2,l3
        carry=0
        
        while True:
            '''
            1 先合并正常对应的部分
            2 再处理 单侧的情形
            3 退出时 检查是否需要补最后节点。
            
            '''
            if p1 and p2:
                s=p1.val+p2.val+carry
                carry=s//10
                p3.next = ListNode(s%10)
                p1,p2,p3 = p1.next,p2.next,p3.next
            elif not p1 and p2:
                s=carry+p2.val
                carry=s//10
                p3.next = ListNode(s%10)
                p2,p3 = p2.next,p3.next
            elif not p2 and p1:
                s=carry+p1.val
                carry=s//10
                p3.next = ListNode(s%10)
                p1,p3 = p1.next,p3.next
            else:
                if carry == 1:
                    p3.next=ListNode(1)
                break
                
        return l3.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        