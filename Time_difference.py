import numpy as np
from time import process_time
pylist=[i for i in range(100)]
start=process_time()
pylist=[i+5 for i in pylist]
end=process_time()
print("Time taken by python list:",end-start)
pyarray=np.array(pylist)
start1=process_time()
pyarray=pyarray+5
end1=process_time()
print("Time taken by numpy array:",end1-start1)
