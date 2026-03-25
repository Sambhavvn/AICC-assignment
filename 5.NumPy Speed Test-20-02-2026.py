import time
import numpy as np

n = 1_000_000

py_list = list(range(n))
np_array = np.arange(n)

start = time.time()
py_result = [x * 2 for x in py_list]
py_time = time.time() - start

start = time.time()
np_result = np_array * 2
np_time = time.time() - start

print("List time:", py_time)
print("NumPy time:", np_time)