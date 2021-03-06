import math
import numpy as np

width = 4
sigma = 2

ret = np.zeros(shape=(2*width + 1, 2*width + 1))

for i in range(-width,width + 1):
    for j in range(-width, width + 1):
        ret[i+width][j+width] = math.exp(-(i*i+j*j)/(2*sigma*sigma))

np.save('2dGaussian.npy',ret)