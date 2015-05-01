'''
Created on Mar 11, 2015

@author: Supreme
'''
from random import shuffle, randint

import time

class Bozo():
    
    def bozo_to_N(self, n):
        
        print("N\tBozo's\tseconds")
        reps = 3
        for i in range(2, n + 1):
            
            avg = 0
            
            for c in range(0,reps):
                bozo_list = [j for j in range(0,i)]
                
                while(sorted(bozo_list) == bozo_list):
                    shuffle(bozo_list)
    
                            
                '''
                Time here
                '''
                count = 0
                start = time.time()
                while sorted(bozo_list) != bozo_list:
                    first_index = randint(0,i -1)
                    second_index = randint(0,i-1)
                    bozo_list[first_index], bozo_list[second_index] = bozo_list[second_index], bozo_list[first_index]
                    count += 1
                
                end = time.time()
                
                avg += end - start
            #print("%d\t%d\t%s" % (i, count, (end-start)))
            print("%d\t%d\t%s" % (i, count, (avg / reps))) 
             
                         
if __name__ == '__main__':
    a =  Bozo()
    a.bozo_to_N(11)
    