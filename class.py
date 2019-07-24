# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:57:03 2019

@author: halid
"""
#%%
class fruit:
         size='Small'
         def __init__(self,color,shape):
                self.color=color
                self.shape=shape
         def salutation(self):
                print(f"I am {self.color} and {self.shape} shaped")
#%%
f = fruit('blue','cube')
f.salutation()