#np.random.randint(33 ,44, 100)

# low, high , size
import numpy as np
from collections import defaultdict

hist = defaultdict(int)

random_age = np.random.randint(35, 44, 100)


for i in random_age:    
    hist[i] += 1

print(hist)

sum_ages = 0
for key, value in hist.items():
    sum_ages += value

bins = [key for key, _ in hist.items()]
pmf = [value  / sum_ages for _, value in hist.items()]
print(bins, pmf)