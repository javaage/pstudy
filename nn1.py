import numpy as np
import matplotlib as plt

x = np.random.uniform(0,1,20)
def f(x): return x * 2
noise_variance = 0.2
noise = np.random.randn()