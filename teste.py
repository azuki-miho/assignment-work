from mydns import *
from gal_dns import *
import pywt
from ellipse import *

orge = []
for i in range(200):
	e1,e2 = elli(galarray0[i])
	e = (e1,e2)
	orge.append(e)

sige = []	
for i in range(200):
	e1,e2 = elli(galarray[i])
	e = (e1,e2)
	sige.append(e)

varsig = 0
for i in range(200):
	s1 = (sige[i][0]-orge[i][0])/orge[i][0]
	s2 = (sige[i][1]-orge[i][1])/orge[i][1]
	var = s1**2 + s2**2
	varsig += var

print("This is the variance of the signal")
print(varsig)
#testsnr for lpdn
min_var = 0
for j in range(40):
	varlp = 0
	for i in range(200):
		lpimage = lpdn(galarray[i],r=j+3)
		lpimage = wndn(lpimage)
		lpimage = wndn(lpimage)
		lpimage = wndn(lpimage)
		lpimage = wndn(lpimage)
		(e1,e2) = elli(lpimage)
		s1 = (e1-orge[i][0])/orge[i][0]
		s2 = (e2-orge[i][1])/orge[i][1]
		s = s1**2 + s2**2
		varlp += s
	if (min_var == 0):
		min_var = varlp
		print("This is the variance for the lpdn")
		print(varlp);print(j+1)
	else:
		if (varlp <= min_var):
			min_var = varlp
			print("This is the variance for the lpdn")
			print(varlp);print(j+1)
			
#testsnr for wndn
varwn = 0
for i in range(200):
	wnimage = wndn(galarray[i])
	(e1,e2) = elli(wnimage)
	s1 = (e1-orge[i][0])/orge[i][0]
	s2 = (e2-orge[i][1])/orge[i][1]
	s = s1**2 + s2**2
	varwn += s
print("This is the variance for the wndn")
print(varwn)

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
