# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:53:50 2019

@author: halid
"""

#%% 
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
#%%
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

