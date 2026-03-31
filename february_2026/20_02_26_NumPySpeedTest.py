# 20/02/26
# NumPy Speed Test

import numpy as np
import time

# Step 1: Get user input for array size
size = int(input("Enter array size: "))

# Step 2: Test NumPy speed
np_array = np.arange(size)
start = time.time()
np_sum = np.sum(np_array ** 2)
np_time = time.time() - start

# Test list speed
py_list = list(range(size))
start = time.time()
py_sum = sum(x ** 2 for x in py_list)
py_time = time.time() - start

# Step 3: Output the results
print("Input:", size)
print("Processed Data:", f"NumPy time: {np_time:.6f}s, List time: {py_time:.6f}s")
if np_time > 0:
    print("Result:", f"NumPy is {py_time / np_time:.2f}x faster")
elif py_time > 0:
    print("Result:", "NumPy was too fast to measure (near instant); list was slower")
else:
    print("Result:", "Both completed too fast to measure meaningfully")
print("Explanation:", "NumPy operations are optimized for performance compared to standard Python lists.")