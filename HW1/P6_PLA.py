import numpy
import matplotlib.pyplot as plt
import random
def sign(number):
	return 1 if number > 0 else -1 # sign function
f = open('hw1_6_train.dat')
content = list(map(lambda s: (numpy.array([1] + list(map(float, s.split()[:4]))), int(s.split()[4])), f.read().strip().split('\n') ))
#reading input and stored x, y as tuple, while x is of type numpy.ndarray
update_cnt = []
for i in range(1126):
	w = numpy.zeros(5) # initializing the starting vector
	random.seed(random.randint(0, 10**10)) #random seed
	random.shuffle(content) # shuffle data to create random cycle
	cnt = 0
	while True:
		flag = False
		for element in content:
			if sign(numpy.inner(w, element[0])) < 0 and element[1] > 0:
				w += element[0]
				cnt += 1
				flag = True
			elif sign(numpy.inner(w, element[0])) > 0 and element[1] < 0:
				w -= element[0]
				cnt += 1
				flag = True
		if not flag:
			break
	update_cnt.append(cnt)
#below is the code for plotting a histogram
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Number of updates')
plt.ylabel('Frequency')
plt.title('Problem 6 PLA\n'+'average number of updates = '+str(sum(update_cnt) / len(update_cnt)))
plt.hist(update_cnt, bins=20)
plt.show(block=True)