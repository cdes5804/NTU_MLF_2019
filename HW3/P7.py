import matplotlib.pyplot as plt
import numpy as np

def sign(num):
	return 1 if num > 0 else -1

def get_data(data_name):
	f = open(data_name, "r")
	return list(map(lambda s: (np.array([1] + list(map(float, s.split()[:20]))), int(s.split()[20])), f.read().strip().split('\n')))

def sigmoid(s):
	return 1.0 / (1 + np.exp(-s))

def gradient(w, data):
	return sum(list(map(lambda s: np.dot(sigmoid(-s[1] * np.dot(w, s[0])), np.dot(-s[1], s[0])), data))) / len(data)

def get_error(w, data):
	return sum(list(map(lambda s: int(sign(sigmoid(np.dot(w, s[0])) - 0.5) != s[1]), data))) / len(data)

train = get_data('hw3_train.dat')
test = get_data('hw3_test.dat')
w_GD, w_SGD = np.zeros(21), np.zeros(21)
E_in_GD, E_in_SGD, = list(), list()
GD_LR, SGD_LR = 0.01, 0.001
for t in range(2000):
	w_GD = w_GD - GD_LR * gradient(w_GD, train)
	E_in_GD.append(get_error(w_GD, train))

	w_SGD = w_SGD + SGD_LR * np.dot(sigmoid(-train[t % 1000][1] * np.dot(w_SGD, train[t % 1000][0])), np.dot(train[t % 1000][1], train[t % 1000][0]))
	E_in_SGD.append(get_error(w_SGD, train))

axis = [t for t in range(1, 2001)]
plt.plot(axis, E_in_GD, 'orange', label = "Batch")
plt.plot(axis, E_in_SGD, 'b', label = "Stochastic")
plt.title("Problem 7")
plt.xlabel("$t$")
plt.ylabel("$E_{in}$")
plt.legend()
plt.show(block=True)