# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:55:09 2017

@author: mustafa
"""
'''Here are the basic facts and terms to know about binary trees:
The convention for binary tree diagrams is that the root is at the top, and the 
subtrees branch down from it.

A node's left and right subtrees are referred to as children, and that node can be 
referred to as the parent of those subtrees.

A non-root node with no children is called a leaf.

Some node 'a' is an ancestor of some node 'b' if 'b' is located in a left or right subtree 
whose root node is 'a'. This means that the root node of binary tree 't' is the ancestor 
of all other nodes in the tree.

If some node 'a' is an ancestor of some node 'b', then the path from 'a' to 'b' is the sequence of
nodes starting with 'a', moving down the ancestral chain of children, and ending with 'b'.

The depth (or level) of some node 'a' is its distance (i.e., number of edges) from the
tree's root node.

Simply put, the height of a tree is the number of edges between the root node and 
its furthest leaf. More technically put, it's 1 + max(height(leftSubtree),height(rightSubtree))  
(i.e., one more than the maximum of the heights of its left and right subtrees).
Any node has a height of , and the height of an empty subtree is -1. Because the height 
of each node is 1 + the maximum height of its subtrees and an empty subtree's height is -1,
the height of a single-element tree or leaf node is 0.'''

'''A Binary Search Tree (BST), , is a binary tree that is either empty or satisfies
 the following three conditions:

Each element in the left subtree of 't' is less than or equal to the root element of 't' (i.e., ).
max(leftTree(t).value) <= t.value)

Each element in the right subtree of 't' is greater than the root element of 't' (i.e., ).
max(rightTree(t).value) > t.value)

Both leftTree(t) and rightTree(t) are BSTs.

You can essentially think of it as a regular binary tree where for each node parent 
having a leftChild and rightChild, leftChild.value <= parent.value < rightChild.value.
'''

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
    
    def getHeight(self,root):
        if root == None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        
T = int(input())  
myTree = Solution()
root = None

for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
    height = myTree.getHeight(root)
print(height)    

'''input
7
3
5
2
1
4
6
7''' 
#output is 3
