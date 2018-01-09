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




