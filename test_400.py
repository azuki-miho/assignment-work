from mydns import *
from gal_400 import *
import pywt
from ellipse import *
import numpy as np
import matplotlib.pyplot as plt
gal1e1arr = []
gal1e2arr = []
gal2e1arr = []
gal2e2arr = []
gal3e1arr = []
gal3e2arr = []
gal4e1arr = []
gal4e2arr = []
for i in range(200):
	e1,e2 = elli(galarray10[i])
	gal1e1arr.append(e1)
	gal1e2arr.append(e2)
for i in range(200):
	e1,e2 = elli(galarray20[i])
	gal2e1arr.append(e1)
	gal2e2arr.append(e2)
for i in range(200):
	e1,e2 = elli(galarray30[i])
	gal3e1arr.append(e1)
	gal3e2arr.append(e2)
for i in range(200):
	e1,e2 = elli(galarray40[i])
	gal4e1arr.append(e1)
	gal4e2arr.append(e2)

gal1e1arr = np.array(gal1e1arr)
gal1e2arr = np.array(gal1e2arr)
gal2e1arr = np.array(gal2e1arr)
gal2e2arr = np.array(gal2e2arr)
gal3e1arr = np.array(gal3e1arr)
gal3e2arr = np.array(gal3e2arr)
gal4e1arr = np.array(gal4e1arr)
gal4e2arr = np.array(gal4e2arr)

gal1sige1 = []
gal1sige2 = []
gal2sige1 = []
gal2sige2 = []
gal3sige1 = []
gal3sige2 = []
gal4sige1 = []
gal4sige2 = []
for i in range(200):
	e1,e2 = elli(galarray1[i])
	gal1sige1.append(e1)
	gal1sige2.append(e2)
gal1sige1 = np.array(gal1sige1)
gal1sige2 = np.array(gal1sige2)
for i in range(200):
	e1,e2 = elli(galarray2[i])
	gal2sige1.append(e1)
	gal2sige2.append(e2)
gal2sige1 = np.array(gal2sige1)
gal2sige2 = np.array(gal2sige2)
for i in range(200):
	e1,e2 = elli(galarray3[i])
	gal3sige1.append(e1)
	gal3sige2.append(e2)
gal3sige1 = np.array(gal3sige1)
gal3sige2 = np.array(gal3sige2)
for i in range(200):
	e1,e2 = elli(galarray4[i])
	gal4sige1.append(e1)
	gal4sige2.append(e2)
gal4sige1 = np.array(gal4sige1)
gal4sige2 = np.array(gal4sige2)
"""
varsig = 0
for i in range(200):
	s1 = (sige[i][0]-orge[i][0])/orge[i][0]
	s2 = (sige[i][1]-orge[i][1])/orge[i][1]
	var = s1**2 + s2**2
	varsig += var
"""



"""
print("This is the variance of the signal")
print(varsig)
#testsnr for lpdn
min_var = 0
elp = []
for j in range(40):
	varlp = 0
	for i in range(200):
		lpimage = lpdn(galarray[i],r=j+3)
		(e1,e2) = elli(lpimage)
"""			
#testsnr for wndn
gal1wne1 = []
gal1wne2 = []
gal2wne1 = []
gal2wne2 = []
gal3wne1 = []
gal3wne2 = []
gal4wne1 = []
gal4wne2 = []
for i in range(200):
	gal1wnimage = wndn(galarray1[i])
	(e1,e2) = elli(gal1wnimage)
	if (e1**2 < 1):
		{
		gal1wne1.append(e1)
		}
	else:
		{
		gal1wne1.append(0)
		}
gal1wne1 = np.array(gal1wne1)
gal1wne2 = np.array(gal1wne2)

plt.figure()
plt.scatter(gal1e1arr,gal1wne1)
plt.show()
for i in range(200):
	gal2wnimage = wndn(galarray2[i])
	(e1,e2) = elli(gal2wnimage)
	if (e1**2 < 1):
		{
		gal2wne1.append(e1)
		}
	else:
		{
		gal2wne1.append(0)
		}
gal2wne1 = np.array(gal2wne1)
gal2wne2 = np.array(gal2wne2)

plt.figure()
plt.scatter(gal2e1arr,gal2wne1)
plt.show()
for i in range(200):
	gal3wnimage = wndn(galarray3[i])
	(e1,e2) = elli(gal3wnimage)
	if (e1**2 < 1):
		{
		gal3wne1.append(e1)
		}
	else:
		{
		gal3wne1.append(0)
		}
gal3wne1 = np.array(gal3wne1)
gal3wne2 = np.array(gal3wne2)

plt.figure()
plt.scatter(gal3e1arr,gal3wne1)
plt.show()
for i in range(200):
	gal4wnimage = wndn(galarray4[i])
	(e1,e2) = elli(gal4wnimage)
	if (e1**2 < 1):
		{
		gal4wne1.append(e1)
		}
	else:
		{
		gal4wne1.append(0)
		}
gal4wne1 = np.array(gal4wne1)
gal4wne2 = np.array(gal4wne2)

plt.figure()
plt.scatter(gal4e1arr,gal4wne1)
plt.show()

	
"""
#testsnr for mvdn
min_var = 0
for k in range(4):
	varmv = 0
	for i in range(200):
		mvimage = mvdn(galarray[i],rg=k+1)
		(e1,e2) = elli(mvimage)
		s1 = (e1-orge[i][0])/orge[i][0]
		s2 = (e2-orge[i][1])/orge[i][1]
		s = s1**2 + s2**2
		varmv += s
	if (min_var == 0):
		min_var = varmv
		print("This is the variance for the mvdn")
		print(varmv);print(k+1)
	else:
		if (varmv <= min_var):
			min_var = varmv
			print("This is the variance for the mvdn")
			print(varmv);print(k+1)

#testsnr for wldn1
min_var = 0
for j in range(5):
	varwl1 = 0
	for i in range(200):
		wlimage1 = wldn1(galarray[i],k=j)
		(e1,e2) = elli(wlimage1)
		s1 = (e1-orge[i][0])/orge[i][0]
		s2 = (e2-orge[i][1])/orge[i][1]
		s = s1**2 + s2**2
		varwl1 += s
	if (min_var == 0):
		min_var = varwl1
		print("This is the variance for the wldn1")
		print(varwl1);print(j+1)
	else:
		if (varwl1 <= min_var):
			min_var = varwl1
			print("This is the variance for the wldn1")
			print(varwl1);print(j+1)
#testsnr for wldn2
wls = pywt.wavelist()[0:15]+pywt.wavelist()[24:80]+[pywt.wavelist()[89],]
wls = wls + pywt.wavelist()[92:107]+pywt.wavelist()[108:]
min_var = 0
for j in range(len(wls)):
	for k in range(5):
		varwl2 = 0
		for i in range(200):
			wlimage2 = wldn2(galarray[i],rat=k/10.,wav=wls[j])
			(e1,e2) = elli(wlimage2)
			s1 = (e1-orge[i][0])/orge[i][0]
			s2 = (e2-orge[i][1])/orge[i][1]
			s = s1**2 + s2**2
			varwl2 += s
		if (min_var == 0):
			min_var =varwl2
			print("This is the variance for the");print(wls[j]);print(varwl2)
			print(k/10.)
		else:
			if (varwl2 <= min_var):
				min_var =varwl2
				print("This is the variance for the");print(wls[j])
				print(varwl2);print(k/10.)
"""
