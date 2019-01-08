import mmh3

# Define hash functions
#h = [blake2b(), md5(), sha1(), sha224(), sha256(), sha384(), sha3_224(), sha3_256(), sha3_384(), sha3_512()]
# Define B with size n = 6 million bits (almost 14 times m) --> k = 10
#B_bin = format(0, '#06000000b')
#B_dec = int(B_bin, 2)
B_dec = 0
n = 6124450

#reading files
path1=r'C:\Users\pegah\Desktop\univ\Courses\data mining\HW5\P2\listed_username_30.txt'
path2=r'C:\Users\pegah\Desktop\univ\Courses\data mining\HW5\P2\listed_username_365.txt'
with open(path1,encoding="utf8") as f:
    content30 = f.readlines()
content30 = [x.strip('\n') for x in content30]
with open(path2,encoding="utf8") as f:
    content365 = f.readlines()
content365 = [x.strip('\n') for x in content365]

k=10
# Filling B with S (content30)
for i in range(len(content30)):
    for j in range(k):
        hash_dec = mmh3.hash(content30[i],j, signed=False)%(2^n)
        B_dec = hash_dec | B_dec

# Checing spams from content365
spam = []
flag = False
test = 0
for i in range(len(content365)):
    for j in range(k):
        hash_dec = mmh3.hash(content365[i],j, signed=False)%(2^n)
        test = hash_dec | test
    for c in range(len(format(test, 'b'))):
        if format(test, 'b')[c]==str(1):
            if format(B_dec, 'b')[c] != str(1):
                flag = True
    if flag:
        flag = False
        continue
    spam.append(content365[i])

#print(len(spam))
#print(type(spam))
#print(spam[:10])

# False-positive rate
false_positive = len(set(spam)) - len(list(set(content30).intersection(spam)))
true_negative = len(content365) - len(spam)
false_positive_rate = false_positive / (true_negative + false_positive)

print('optimal k for n = {0} is {1}'.format(n, k))
print('false positive rate (false postive/(false positive + true negative)) is {0:0.4f}'.format(false_positive_rate))
