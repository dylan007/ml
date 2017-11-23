import csv
import random
import math
import operator


def loadDataset(filename, split, training, test):
	with open(filename,'rb') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for i in range(len(dataset)-1):
			for j in range(4):
				dataset[i][j] = float(dataset[i][j])
			if random.random() < split:
				training.append(dataset[i])
			else:
				test.append(dataset[j])


def EuclidDist(a,b,l):
	ans = 0
	for i in range(l):
		ans += (a[i]-b[i]) ** 2
	return math.sqrt(ans)

def getNeighbors(train,test,k):
	dist = []
	for i in range(len(train)):
		dist.append((i,EuclidDist(train[i],test,len(test)-1)))
	dist.sort(key = operator.itemgetter(1))
	res = []
	for i in range(k):
		res.append(train[dist[i][0]][len(test)-1])
	return res


def classify(res):
	resSet = list(set(res))
	l = []
	for i in range(len(resSet)):
		l.append((resSet[i],res.count(resSet[i])))
	l.sort(key = operator.itemgetter(1),reverse = True)
	return l[0][0]

def getAccurracy(predictions,testdata):
	c = 0.0
	w = 0.0
	for i in range(len(predictions)):
		if(predictions[i] == testdata[i]):
			c += 1.0
		else:
			w += 1.0
	return "Accuracy is " + str(c/(c+w))

def main():
	train = []
	test = []
	loadDataset('iris.data',0.67,train,test)
	print len(train),len(test),len(train)+len(test)
	predictions = []
	testdata = []
	for i in range(len(test)):
		testdata.append(test[i][4])
		predictions.append(classify(getNeighbors(train,test[i],4)))
	print getAccurracy(predictions,testdata)

main()