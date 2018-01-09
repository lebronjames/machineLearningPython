import csv     #用于处理csv文件
import random    #用于随机数
import math
import operator  #
from sklearn import neighbors

#计算距离
def euclideanDistance(instance1,instance2):
    distance = 0
    for x in range(4):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

#返回K个最近邻
def getNeighbors(trainingSet,testInstance,k):
    distances = []
    # 计算每一个测试实例到训练集实例的距离
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x])
        distances.append((trainingSet[x], dist))
    # 对所有的距离进行排序
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    # 返回k个最近邻
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#对k个近邻进行合并，返回value最大的key
def getResult(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    # 排序
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def main():
    trainingSet = []  # 训练数据集
    testSet = []  # 测试数据集
    splitRatio = 0.75  # 分割的比例
    filename = r"./iris.txt"
    with open(filename,'rt') as datafile:
        lines = csv.reader(datafile)
        print("-------------------",lines)
        dataSet = list(lines)
        for x in range(len(dataSet)-1):
            for y in range(4):
                dataSet[x][y] = float(dataSet[x][y])
            if(random.random() < splitRatio):
                trainingSet.append(dataSet[x])
            else:
                testSet.append(dataSet[x])
    print("trainingSet len:",len(trainingSet))
    print("testSet len:", len(testSet))

    results = []
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainingSet,testSet[i],3)
        result = getResult(neighbors)
        results.append(result)
        print("期望值：",testSet[i][-1],"实际值：",result)
    correct = 0
    for i in range(len(results)):
        if(results[i] == testSet[i][-1]):
            correct += 1
    print("准确率：",correct/float(len(results))*100,"%")

main()