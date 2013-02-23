#!/usr/bin/python

import csv, numpy
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def compareScatter(file1,keycol1,valcol1,file2,keycol2,valcol2,file3,keycol3,valcol3):
	reader=csv.reader(file("./Datasets/"+file1))
	headerRow=reader.next()
	a_file1=numpy.array(list(reader))
	
	reader=csv.reader(file("./Datasets/"+file2))
	headerRow=reader.next()
	a_file2=numpy.array(list(reader))
	
	reader=csv.reader(file("./Datasets/"+file3))
	headerRow=reader.next()
	a_file3=numpy.array(list(reader))
	
	a_file1_slice=a_file1[:,keycol1-1],a_file1[:,valcol1-1]
	a_file2_slice=a_file2[:,keycol2-1],a_file2[:,valcol2-1]
	a_file3_slice=a_file3[:,keycol3-1],a_file3[:,valcol3-1]
	
	d_file1=dict(zip(*a_file1_slice))
	d_file2=dict(zip(*a_file2_slice))
	d_file3=dict(zip(*a_file3_slice))
	
	a_joined=numpy.array([(k,d_file1.get(k),d_file2.get(k),d_file3.get(k))
	               for k in set(d_file1.iterkeys()).union(d_file2.iterkeys()).union(d_file3.iterkeys())])
	
	
	x=map(float,a_joined[:,1])
	y=map(float,a_joined[:,2])
	z=map(float,a_joined[:,3])
	
	return x,y,z


a_education,a_employment,a_health=compareScatter("education2010.csv",1,6,"employment2010.csv",1,6,"health2010.csv",1,6)

ax=subplot(221)
ax.scatter(a_education,a_employment,s=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title("Education vs employment")
ax.set_xlabel("Education")
ax.set_ylabel("Employment")

ax=subplot(222)
ax.scatter(a_education,a_health,s=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title("Education vs health")
ax.set_xlabel("Education")
ax.set_ylabel("Health")

ax=subplot(223)
ax.scatter(a_employment,a_health,s=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title("Employment vs health")
ax.set_xlabel("Employment")
ax.set_ylabel("Health")

ax=subplot(224,projection='3d')
ax.scatter(a_education,a_employment,a_health,s=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.set_title("Employment vs education vs health")
ax.set_xlabel("Education")
ax.set_ylabel("Employment")
ax.set_zlabel("Health")
	
show()



