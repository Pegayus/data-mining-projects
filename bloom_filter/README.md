## Bloom Filter
Implementation of the Bloom filter. I have used [this dataset](http://www.stopforumspam.com/downloads/listed_username_30.zip
) as the set of usernames known to be spam for the last 30 days. 

version 1:
I have used [murmurHash function](https://sites.google.com/site/murmurhash/) with hashing memory size n and found the optimal number of hash functions (k). My stream is the spam usernames for the last 365 days is taken from [here](http://www.stopforumspam.com/downloads/listed_username_365.zip)

version 2: 
I have implemented Bloom filtering on the same stream using built-in Python library [bloom-filter](https://pypi.org/project/bloom-filter/).

Output:
1. Optimal K for my selected n
2. Percentage of false positives 
