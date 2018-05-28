# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:51:40 2017

@author: mustafa
"""
'''Tree Traversal
A traversal of some binary tree,t , is an algorithm that iterates through each 
node in t exactly 1 time.

InOrder Traversal
An inorder traversal of tree t is a recursive algorithm that follows the left 
subtree; once there are no more left subtrees to process, we process the right 
subtree. The elements are processed in left-root-right order.
An inorder traversal of a binary search tree will process the tree's elements in 
ascending order.

PostOrder Traversal
A postorder traversal of tree t is a recursive algorithm that follows the left and 
right subtrees before processing the root element. The elements are processed in 
left-right-root order. 

PreOrder Traversal (DFS)
A preorder traversal of tree t is a recursive algorithm that processes the root and 
then performs preorder traversals of the left and right subtrees. The elements are 
processed root-left-right order.
Because a preorder traversal goes as deeply to the left as possible, 
it's also known as a depth-first-search or DFS.

Level-Order Traversal (BFS)
A level-order traversal of tree t is a recursive algorithm that processes the root, 
followed by the children of the root (from left to right), followed by the 
grandchildren of the root (from left to right), etc. 
Because a level-order traversal goes level-by-level, 
it's also known as a breadth-first-search (BFS)

    '''
import collections
class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data<=root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root
        
    def levelOrder(self,root):
        queue = [root] if root else []
        
        for current in queue:    
            if current:
                print(current.data, end=' ')

                queue.append(current.left)
                queue.append(current.right)
        '''while queue:
            node = queue.pop()
            print(node.data, end=" ") 
            
            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)'''
    def InOrder(self,root):
        res = []
        while root:
            self.insert(root.left,res)
            res.append(root.data)
            self.insert(root.right,res)  
            print(list(res))
            
    def PostOrder(self,root):
        pass
    def PreOrder(self,root):
        pass
        
T = int(input())  
myTree = Solution()
root = None

for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)
myTree.InOrder(root)