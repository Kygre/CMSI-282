'''
Created on Jan 23, 2015

@author: Kwadwo Yeboah

A first principle implementation of a Priority Queue
'''
from math import floor


class PriorityQueue():
    
    def __init__(self):
        self.__myHeap = []        
         
     
    def add(self, obj):
        self.__myHeap.append(obj)
        self.siftUp(self.__len__() - 1)
        return self
    
    def peek(self):
        return self.__myHeap[0]
    
    def remove(self):
        
        if self.__myHeap.__len__() == 0:
            raise Exception("Cannot remove from empty Priority Queue")
    
        last_pop = self.peek()
        
        if self.__myHeap.__len__() == 1:
            self.__myHeap = []         
        else:
            self.__myHeap[0] = self.__myHeap.pop()        
            self.siftDown(0)
            
        return last_pop
    
    def siftDown(self, index):
        
        child_index = index * 2 + 1
        
        if child_index >= self.__myHeap.__len__():
            return
        
        
        if child_index + 1 < self.__myHeap.__len__():
            
            if self.__myHeap[child_index] > self.__myHeap[child_index + 1]:
                child_index += 1
            
                  
        if self.__myHeap[child_index] < self.__myHeap[index]:
                
                self.__myHeap[index], self.__myHeap[child_index] = self.__myHeap[child_index], self.__myHeap[index]
                self.siftDown(child_index)
        
        
        
    def siftUp(self, index):
        
        parent = ((index - 1) // 2)
        
        if(parent >= 0 and self.__myHeap[index] < self.__myHeap[parent]):
            
            self.__myHeap[index], self.__myHeap[parent] = self.__myHeap[parent], self.__myHeap[index]
            self.siftUp(parent)
        
    
    
    def empty(self):
        return self.__len__() == 0
    
    def __len__(self):
        return self.__myHeap.__len__()
    def __str__(self):
        
        return self.__myHeap.__str__()

