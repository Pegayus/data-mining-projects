
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets
#read dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target
target_names = iris.target_names
#pca
pca = decomposition.PCA(n_components=2)
x = pca.fit(x).transform(x)
#plot
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(x[y == i, 0], x[y == i, 1], color=color, alpha=.8, lw=2,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.show()







