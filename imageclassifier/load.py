import cPickle as pickle
import numpy as np 
import subprocess
import sys


def load(filename):
	with open(filename) as f:
		data = pickle.load(f)
		return np.asarray(data['data']),np.asarray(data['labels'])