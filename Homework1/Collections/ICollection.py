'''
Created on Jan 23, 2015

@author: Kwadwo Yeboah
Contains all superclasses for the 
'''
import abc

class ICollection( metaclass = abc.ABCMeta):
    '''
    A superclass for collections 
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @abc.abstractmethod
    def add(self, obj):
        raise NotImplementedError("Please Implement add")
    
    @abc.abstractmethod
    def empty(self):
        raise NotImplementedError("Please Implement empty")
    
    @abc.abstractmethod
    def size(self):
        raise NotImplementedError("Please Implement size")
    
    
    