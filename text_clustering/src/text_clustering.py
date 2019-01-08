
# coding: utf-8

# In[91]:

#read data
import re
import numpy as np
path=r'C:\Users\pegah\Desktop\univ\courses\data mining\HW3\foods.txt'
with open(path) as f:
    text=f.readlines()
text=[x.strip() for x in text]
path2=r'C:\Users\pegah\Desktop\univ\courses\data mining\HW3\LongStopwordList.txt'
with open(path2) as f:
    stops=f.readlines()
stops=[x.strip() for x in stops]


# In[92]:

#extract reviews
review=[]
for i in range(len(text)):
    if text[i][0:13]=='review/text: ':
        review.append(text[i].split('review/text: ',1)[1])          


# In[93]:

#get unique words from reviews
#L=unique_words
unique_words=set()
for i in range(len(review)):
    polished_review= re.sub('[^a-zA-Z]+', ' ', review[i])   #replace all non-alphabet char with space
    words=re.findall(r"[\w']+", polished_review)            #split string into unique words by putting them into a set
    unique_words.update(words)


# In[94]:

#remove stopwords 
#W=polished_words
polished_words=unique_words.difference(stops)
W=list(polished_words)
W_lowerCase=[x.lower() for x in W]
W_lower_reduced=W_lowerCase
for word in stops:
     W_lower_reduced = [x for x in W_lower_reduced if x != word]


# In[95]:

#get top 500 words
total_words=[]
for i in range(len(review)):
    polished_review= re.sub('[^a-zA-Z]+', ' ', review[i])   #replace all non-alphabet char with space
    words=re.findall(r"[\w']+", polished_review)            #split string into its words
    total_words.extend(words)
tot_word_lowerCase=[x.lower() for x in total_words]

#W_tot_reduced=tot_word_lowerCase
for word in stops:
    W_tot_reduced = [x for x in W_tot_reduced if x != word]

#remove br
W_tot_reduced = [x for x in W_tot_reduced if x != 'br']

import collections
freq=collections.Counter(W_tot_reduced).most_common(500)


# In[234]:

#output the 500 top words
with open("500CommonWords.txt", "w") as output:
    output.write(str(freq))


# In[255]:

#make 500 words into features
features=[]
for i in range(len(freq)):
    features.append(freq[i][0])


# In[271]:

#making feature dictionary for sklearn feature extraction
data=[]
for i in range(len(review)):
    polished_review= re.sub('[^a-zA-Z]+', ' ', review[i])
    wr=polished_review.split()
    a=collections.Counter(wr)
    anew={}
    for word in a.keys():
        if word in features:
            anew[word]=a[word]
    data.append(anew)


# In[273]:

#vectorizing
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
vec_data=vec.fit_transform(data).toarray()


# In[276]:

#kmeans
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=10, random_state=0).fit(vec_data)


# In[299]:

#saving features and centers in order
FName=vec.get_feature_names()
centers=kmeans.cluster_centers_

#soritng and getting the final result
sort={}
for i in range(len(centers)):
     sort[i]=np.argsort(centers[i])[::-1][:5]

result={}
for i in range(len(sort)):
    result[i]=[(FName[x],centers[i][x]) for x in sort[i]]
                   


# In[307]:

#output the kmeans result
with open("CentroidsTop5Words.txt", "w") as output:
    output.write(str(result))


# In[ ]:



