#!/usr/bin/env python
# coding: utf-8

# ## Assignment-9 (Letters Count)

# In[4]:


sentences = input("Enter a sentence: ")
sentences = s.strip().lower()
dictionary = {}
for i in set(sentences):
   dictionary[i] = sentences.count(i)
print(dictionary) 


# In[ ]:




