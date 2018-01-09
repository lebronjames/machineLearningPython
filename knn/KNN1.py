from sklearn import neighbors
#from sklearn import datasets
from sklearn.datasets import load_iris

knn = neighbors.KNeighborsClassifier() #获取knn分类算法

#iris = datasets.load_iris() #把数据load进来

#查看iris数据集
iris = load_iris()

print(iris)

#训练数据集
#knn.fit(iris.txt,iris.target)

#预测
#predict = knn.predict([[0.1,0.2,0.3,0.4]])

#print(predict)



