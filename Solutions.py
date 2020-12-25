# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:28:33 2020

@author: Weiq
"""
#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#  417  Pacific Atlantic Water Flow
    def pacificAtlantic(self, matrix: list) -> list:
        from collections import deque
        m = len(matrix)
        n = len(matrix[0])
        
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        left_que = deque([(0,a) for a in range(n)] +\
                [(a,0) for a in range(1, m)])
        left = set(left_que)
        right_que = deque([(m-1, a) for a in range(n)]\
                + [(a, n-1) for a in range(m)])
        right = set(right_que)
        
        def check_next(trace, a:tuple, the_set):
            row = trace[0] + a[0]
            column = trace[1] + a[1]
            limit1 = 0<=row<=m-1 and 0<=column<=n-1
            if limit1:
                limit2 = matrix[row][column]>=\
                        matrix[trace[0]][trace[1]] \
                        and (row, column) not in the_set
                if limit2:
                    the_set.add((row, column))
                    return (row, column)                                                             
            return False
                
        
        def process_que(the_que, the_set):
            while the_que:
                for a in range(len(the_que)):
                    trace = the_que.popleft()
                    for b in directions:
                        trace_back = check_next(trace, b, the_set)
                        if trace_back: the_que.append(trace_back)
            
        
        process_que(left_que, left)
        process_que(right_que, right)
        return left, right

# 445. Add Two Numbers II
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNumber(l: ListNode) -> int:
            nextN = l.next
            res = l.val
            while nextN:
                res = res*10 + nextN.val
                nextN = nextN.next
            return res
        def getList(n: int) -> ListNode:
            if not n: return ListNode()
            number = []
            while n:
                n, digit = divmod(n, 10)
                number.append(digit)
            number = [ListNode(val=a) for a in number]
            for a in range(1, len(number)):
                number[a].next = number[a-1]
            return number[-1]
        return getList(getNumber(l1) + getNumber(l2))


        
                    
            
#%%
m = Solution()
# matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# left, right = m.pacificAtlantic(matrix)
# print(left.intersection(right))

            
            
        
        