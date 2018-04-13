import csv
import codecs
#import numpy as np
#import pandas as pd




f = open("S0EP4_fakedata.txt",'r')
file_content0 = []
mark = True
while(mark):
    file_content0.append(f.readline())
    mark = file_content0[-1]
f.close()
print (file_content0)


file_content1 = []
with open ("S0EP4_fakedata.txt") as f:
	mark = True;
	while (mark):
		file_content1.append(f.readline())
		mark = file_content1[-1]

print (file_content1), '\n'


with open ("S0EP4_fakedata.txt") as f:
	file_content2 = f.readlines()

print (file_content2)

with codecs.open ("S0EP4_fakedata2.txt",'r',"utf-8") as f:
	file_content3 = f.readlines()
print (file_content3)

for item in file_content3:
	print (item)

with codecs.open("S0EP4_fakedata2_w.txt","w",encoding='utf-8') as f:
	for item in file_content3:
		f.write(item)

try:
	def file_content0
	def file_content1
	def file_content2
	def file_content3
except Exception
	pass

npdata = np.genfromtxt("S0EP4_fakedata2.txt",skip_header=1,dtype=None,delimiter=',')
#print npdata

print npdata[0][0], len(npdata[0][0]), unicode(npdata[0][0].decode('utf-8')), len(npdata[0][0].decode('utf-8'))
#npdata[0][0], npdata[0][0].decode('utf-8')








a = 3
b = eval('a+2')
print (b)

e = [2]
exec('b'+str(e[0])+'=a**2')
print (b2)

