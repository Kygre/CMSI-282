'''
Created on Jan 23, 2015

@author: Supreme

A first principle implementation of a Red-Black Tree
'''

from _collections_abc import Iterable
from math import floor

from Collections.ICollection import ICollection


class PriorityQueue():
    
    def __init__(self):
        self.myHeap = []        
         
     
    def add(self, obj):
        self.myHeap.append(obj)
        self.siftUp(self.__len__() - 1)
        return self
    def peek(self):
        return self.myHeap[0]
    
    def remove(self):
        first_pop = self.peek()
        if self.myHeap.__len__() > 1:
            self.myHeap[0] = self.myHeap.pop()        
            self.siftDown(0)
        return first_pop
    
    def siftDown(self, index):
        
        child_left_index = index * 2 + 1
        
        smaller_child = None
        
        if child_left_index + 1 < self.myHeap.__len__():
            
            if self.myHeap[child_left_index] < self.myHeap[child_left_index + 1]:
                smaller_child = child_left_index
            else:
                smaller_child = child_left_index + 1
        elif child_left_index < self.myHeap.__len__():
            
            smaller_child = child_left_index 
        
        if smaller_child is not None:
            
            if self.myHeap[smaller_child] < self.myHeap[index]:
                
                self.myHeap[index], self.myHeap[smaller_child] = self.myHeap[smaller_child], self.myHeap[index]
                self.siftDown(smaller_child)
        
        
        
    def siftUp(self, index):
        
        parent = floor((index - 1) / 2)
        
        if(parent >= 0 and self.myHeap[index] < self.myHeap[parent]):
            
            temp = self.myHeap[index]
            self.myHeap[index] = self.myHeap[parent]
            self.myHeap[parent] = temp 
            
            self.siftUp(parent)
        
    
    
    def empty(self):
        return self.__len__() == 0
    
    def __len__(self):
        return self.myHeap.__len__()
    def __str__(self):
        s = "["
        
        first = True
        for value in self.myHeap:
            if first:
                first = False
            else:
                s += ","
            s += str(value) 
            
            
        return self.myHeap.__str__()

    
