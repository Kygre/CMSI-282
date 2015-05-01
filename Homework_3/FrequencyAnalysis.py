'''
Created on Mar 13, 2015

@author: Supreme
'''
from sqlite3 import collections



if __name__ == '__main__':
    
    a = ""
    cipher_text = "UIQLDEVORHIWLTQTOKMQMWROUOQQMQLKIQWQVIEWRDQTLEQMW\nRWXFTWHTOADMRDQIOKWXMAOHMRMRHQVOQWLTAOMRQODPMDQWMRDQTLEQOEWAFLQIT\nBVOQQWKWUIQLDEWREIRQTOQITOQVITWRIJFUO\nMRMRHQWVLAORSIMRHDBVOQBIBORQOEWAFLQITQWKW"
    save = ""
    while a != "!q":
        
        print("Cipher is %s" % cipher_text)
        print(collections.Counter(cipher_text).most_common(3))
        a = input("Input pair to be replace or !q to quit:\n")
        chars = a.split()
        
        cipher_text = cipher_text.replace(chars[0], chars[1]) 
        

                
        
        
def count_Group_of_n( text , size):
    
    i = 0
    
    while i - size < len(text):
        pass