import operator

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neighbors as sk

myfont = fm.FontProperties(fname=r'c:\windows\fonts\msyh.ttc')


def create():
    datasets = np.array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5], [8, 4, 1], [7, 1, 2], [1, 4, 5], [3, 6, 5]])
    lables = ['非常热', '非常热', '一般热', '一般热', '非常热', '非常热', '一般热', '一般热']
    return datasets, lables


def analyze_data_plot(x, y):
    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.scatter(x, y)

    plt.title('散点图', fontsize=25, fontname='微软雅黑', fontproperties=myfont)
    plt.xlabel('散点图', fontsize=25, fontname='微软雅黑', fontproperties=myfont)
    plt.ylabel('散点图', fontsize=25, fontname='微软雅黑', fontproperties=myfont)

    # plt.savefig('datasets.png',bbox_inches='tight')
    plt.show()


def EulideanDistance(newV, datasets):
    row, col = datasets.shape
    d = np.tile(newV, (row, 1)) - datasets
    sqd = d ** 2
    sqrtd = sqd.sum(axis=1) ** 0.5

    return sqrtd


def knn_classifier(newV, datasets, labels, k):
    sqrtDist = EulideanDistance(newV, datasets)

    sortedDistIndexs = sqrtDist.argsort(axis=0)

    classCount = dict()

    for i in range(k):
        votelabel = labels[sortedDistIndexs[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1))

        return sortedClassCount[0][0]


if __name__ == '__main__':
    datasets, lables = create()

    analyze_data_plot(datasets[:, 0], datasets[:, 1])

    res = knn_classifier([2, 4, 4], datasets, lables, 3)
    print(res)

    #  use knn
    knn = sk.KNeighborsClassifier()

    knn.fit(datasets, lables)

    result = knn.predict([[2, 4, 4]])

    print(result)
