Download the fine foods dataset from:
http://snap.stanford.edu/data/web-FineFoods.html
The following steps are done:
1- Identify all the unique words that appear in the "review/text"  field of the reviews. Denote
the set of such words as L.
2- Remove from L all stopwords in "Long Stopword List" from http://www.ranks.nl/stopwords.
Denote the cleaned set as W.
3- Count the number of times each word in W appears among all reviews ("review/text" field) and identify the top 500 words.
4- Vectorize all reviews ("review/text" field) using these 500 words.
5- Cluster the vectorized reviews into 10 clusters using k-means. You are allowed to use any
program or code for k-means (Weka has k-means too). This will give you 10 centroid
vectors.
6- From each centroid, select the top 5 words that represent the centroid (i.e., the words with
the highest feature values)

Output:
1. Top 500 words + counts for these words
2. The top 5 words representing each cluster and their feature values (50 words + 50
values).