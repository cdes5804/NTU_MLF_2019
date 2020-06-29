import random
import numpy as np
import time
#import matplotlib.pyplot as plt
random.seed(time.time())
np.random.seed(random.randint(0, 2**31))
def sign(x):
    return 1 if x > 0 else -1

def f(x):
    return -sign(x) if random.random() <= 0.2 else sign(x)

def get_error(data):
    cnt = 0
    for element in data:
        if element[1] == -1:
            cnt += 1
    return cnt

dif = []

for _ in range(1000):
    np.random.seed(random.randint(0, 2**31))
    data = [(x, f(x)) for x in np.random.uniform(-1, 1, 2000)]
    data.sort()
    theta = (-1 + data[0][0]) / 2
    positive_err = get_error(data)
    negative_err = len(data) - positive_err
    E_in, s = min(positive_err, negative_err), 1 if positive_err < negative_err else -1
    for i in range(len(data) - 1):
        positive_err += (1 if data[i][1] == 1 else -1)
        negative_err += (1 if data[i][1] == -1 else -1)
        if min(positive_err, negative_err) < E_in:
            E_in, theta, s = min(positive_err, negative_err), (data[i][0] + data[i + 1][0]) / 2, (1 if positive_err < negative_err else -1)
    E_in /= len(data)
    E_out = 0.3 * s * (abs(theta) - 1) + 0.5
    dif.append(E_in - E_out)

print('average is', sum(dif) / len(dif))    
'''plt.grid(axis='y', alpha=0.75)
plt.xlabel(r'$E_{in} - E_{out}$')
plt.ylabel('Frequency')
plt.title('Decision stump with large data size')
plt.hist(dif, bins=20, color='green')
plt.show(block=True)'''