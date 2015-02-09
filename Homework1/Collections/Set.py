'''
Created on Jan 23, 2015

@author: Kwadwo Yeboah

A first principle implementation of a Red-Black Tree
'''
from math import floor


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
        
        if self.myHeap.__len__() == 0:
            raise Exception("Cannot remove from empty Priority Queue")
    
        first_pop = self.peek()
        
        if self.myHeap.__len__() == 1:
            self.myHeap = []         
        else:
            self.myHeap[0] = self.myHeap.pop()        
            self.siftDown(0)
            
        return first_pop
    
    def siftDown(self, index):
        
        child_index = index * 2 + 1
        
        if child_index >= self.myHeap.__len__():
            return
        
        
        if child_index + 1 < self.myHeap.__len__():
            
            if self.myHeap[child_index] > self.myHeap[child_index + 1]:
                child_index += 1
            
                  
        if self.myHeap[child_index] < self.myHeap[index]:
                
                self.myHeap[index], self.myHeap[child_index] = self.myHeap[child_index], self.myHeap[index]
                self.siftDown(child_index)
        
        
        
    def siftUp(self, index):
        
        parent = floor((index - 1) / 2)
        
        if(parent >= 0 and self.myHeap[index] < self.myHeap[parent]):
            
            self.myHeap[index], self.myHeap[parent] = self.myHeap[parent], self.myHeap[index]
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

'''
if __name__ == "__main__":
    
    a = PriorityQueue()
    
    scan = ""
    
    while scan != "q":
        
        
        scan = input("q to quit or add # to push")
        
        if scan != "q":
            
            a.add(int(scan))
            
        elif scan = "p"
            print(str(a.remove())
            
        print(a)
    
'''
    
    
    
    
