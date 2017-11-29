import load
import numpy as np
import scipy.spatial.distance


def loadAll():
	files = ['data_batch_1','data_batch_2','data_batch_3','data_batch_4','data_batch_5']
	path = '/home/dylan/Downloads/cifar-10-batches-py/'
	Xtr = load.load(path + 'data_batch_1')[0]
	Ytr = load.load(path + 'data_batch_1')[1]
	for i in range(1,len(files)):
		p = path + files[i]
		resx,resy = load.load(p)
		print Xtr.shape,resx.shape	
		Xtr = np.concatenate((Xtr,resx))
		Ytr = np.concatenate((Ytr,resy))
	res = load.load(path + 'test_batch')
	return Xtr,Ytr,res[0],res[1]

class knn:
	def __init__(self):
		pass

	def train(self,X,Y):
		self.X = X
		self.Y = Y

	def predict(self,X,k):
		Ypred = []
		for i in range(len(self.X)):
			Ypred.append((scipy.spatial.distance.euclidean(self.X[i],X),self.Y[i]))
		Ypred = sorted(Ypred,key = lambda x:x[0])
		count = [0]*10
		for i in range(len(Ypred)):
			count[Ypred[i][1]] += 1
		return count.index(max(count))


if __name__=='__main__':
	Xtr,Ytr,Xte,Yte = loadAll()
	model = knn()
	model.train(Xtr,Ytr)
	preds = []
	for i in range(len(Xte)):
		print "Predicting data " + str(i) 
		preds.append(model.predict(Xte[i],4))
	print np.mean(preds==Yte)


