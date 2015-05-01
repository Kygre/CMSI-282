'''
Created on Mar 12, 2015

@author: Kwadwo Yeboah

'''
from setuptools.compat import unichr

def encrypt(plain_text, cipher_key):
        keyphrase = cipher_key + plain_text
        keyphrase = keyphrase[:len(plain_text)]
        ans = ""
        
        for i in zip(plain_text, keyphrase):
            ans += unichr(((ord(i[0]) + ord(i[1]) - (65 * 2)) % 26) + 65)
        return ans

if __name__ == '__main__':
    print(encrypt("TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR", "QUARK"))             
    