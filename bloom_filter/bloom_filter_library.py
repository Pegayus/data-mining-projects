
# coding: utf-8

# In[98]:


#pip install bloom_filter
from bloom_filter import BloomFilter
import numpy as np


# In[99]:


#reading files
path1=r'C:\Users\pegah\Desktop\DM_HW5\listed_username_30.txt'
path2=r'C:\Users\pegah\Desktop\DM_HW5\listed_username_365.txt'
with open(path1,encoding="utf8") as f:
    content30 = f.readlines()
content30 = [x.strip('\n') for x in content30]
with open(path2,encoding="utf8") as f:
    content365 = f.readlines()
content365 = [x.strip('\n') for x in content365]


# In[100]:


# defining bloom filter , max_elements = # of elements in content30
# error_rate = expected error rate from the formula (1-e^(-kn/m))^k
# chosen n = (appx) 5 times of max_elements = 2041484
# k = 4 (from formula)
B_filter = BloomFilter(max_elements = len(content30), error_rate = 0.1)
for name in content30:
    B_filter.add(name)
k = np.ceil((B_filter.num_bits_m/len(content30))*np.log(2))


# In[101]:


# testing filter
spam=[]
for name in content365:
    if name in B_filter:
        spam.append(name)


# In[102]:


#false positive rate
false_positive = len(set(spam)) - len(list(set(content30).intersection(spam)))
true_negative = len(content365) - len(spam)
false_positive_rate = false_positive / (true_negative + false_positive)


# In[106]:


print('optimal k for n = {0} is {1}'.format(B_filter.num_bits_m, k))
print('false positive rate (false postive/(false positive + true negative)) is {0:0.4f}'.format(false_positive_rate))
print('deviation of false positive rate from expected value is {:0.4f}'.format(np.abs(false_positive_rate - B_filter.error_rate_p )))

