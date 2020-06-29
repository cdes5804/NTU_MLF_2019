import numpy
import matplotlib.pyplot as plt
import random
def sign(number):
	return 1 if number > 0 else -1 # sign function
def error(cur, content):
	err_cnt = 0
	for element in content:
		if sign(numpy.inner(cur, element[0])) * element[1] < 0:
			err_cnt += 1
	return err_cnt # functions counting number of errors
f = open('hw1_7_train.dat')
f2 = open('hw1_7_test.dat')
content = list(map(lambda s: (numpy.array([1] + list(map(float, s.split()[:4]))), int(s.split()[4])), f.read().strip().split('\n') ))
content2 = list(map(lambda s: (numpy.array([1] + list(map(float, s.split()[:4]))), int(s.split()[4])), f2.read().strip().split('\n') ))
error_rate = []
for i in range(1126):
	w = numpy.zeros(5)
	random.seed(random.randint(0, 10**10))
	random.shuffle(content) # same effect as random cycle
	cnt = 0
	while cnt < 100:
		element = random.choice(content)
		if sign(numpy.inner(w, element[0])) < 0 and element[1] > 0:
			w += element[0]
			cnt += 1
		elif sign(numpy.inner(w, element[0])) > 0 and element[1] < 0:
			w -= element[0]
			cnt += 1
	error_rate.append(error(w, content2) / len(content2))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Error rate')
plt.ylabel('Frequency')
plt.title('Problem 8 W100\n'+'average error rate = '+str(sum(error_rate) / len(error_rate)))
plt.hist(error_rate, bins = 20)
plt.show(block=True)