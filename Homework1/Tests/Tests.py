'''
Created on Jan 25, 2015

@author: Supreme
'''
import unittest
from Collections.Set import PriorityQueue
from random import randint, shuffle

class Test(unittest.TestCase):

    
    def setUp(self):
        self.myPQ = PriorityQueue()
        


    def tearDown(self):
        pass

    def test_empty_Init_PriorityQueue(self):
        a = PriorityQueue()
       
       
        self.assertEqual(0, a.__len__(), "Initiliazed Queue is not empty!")
    
    def test_push_To_Random(self):
        rand_max = randint(10, 1000)
        for i in range(0, rand_max):
            self.myPQ.add(i)
        
        self.assertFalse(self.myPQ.empty(), "Priority Queue is not empty")
        self.assertEqual(self.myPQ.__len__(), rand_max, "Pushed random max = %d not equal to PQ = %d" % (rand_max, self.myPQ.__len__()))
    
    
    def test_pop_Priority_In_Order(self):
        
        pushees = []
        for i in range(0,50): 
            pushees.append(i)
        
        tester = pushees.copy()
        shuffle(pushees)
        
        for i in pushees:
            self.myPQ.add(i)
        
        for i in tester:
            self.assertEqual(i, self.myPQ.remove(), "Queue not prioritized in order")
            
        
if __name__ == "__main__":
    
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    