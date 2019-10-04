import cv2
import math
import numpy as np 
import random

im_a = cv2.imread("template.png",0)
basis_point = (0,0.2)
shape = im_a.shape
basis_point = basis_point[0]*shape[0]/2 + shape[0]/2, basis_point[1]*shape[1]/2 + shape[1]/2

def ray(image, basis_point, angle):
	vector = np.array((math.sin(angle),math.cos(angle)))
	coordinates = np.array([basis_point[0],basis_point[1]])
	distance = 0
	while True:
		if (image.shape<=coordinates).any() or (coordinates<0).any():
			return None
		cr = coordinates.astype(int)
		if image[cr[0]][cr[1]] != 255:
			return distance
		distance += 1
		coordinates = coordinates+vector
def add_noise(x):
	if x!=None:
		x+=np.random.normal()*16
		x*=random.randint(100,104)/102.0
		if random.randint(0,16)<4:
			return None
	return x
print(basis_point)
u_l = []
u_noised = []
v_l = []

for i in range(0,3600):
	v = i/(10*2*math.pi)
	u = ray(im_a, basis_point, v)
	u_noised.append(add_noise(u))
	u_l.append(u)
	v_l.append(v)

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(v_l,u_noised,s=1)
c = ax.scatter(v_l,u_l,s=1)

plt.show()