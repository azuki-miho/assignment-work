from mydns import *
from mygal import *
import pywt

sig=image.array
org=image0.array

osnr = snr(org, sig)
print("This is the snr or the signal")
print(osnr)

#testsnr for lpdn
for j in range(40):
	lpimage = lpdn(sig,r=j+1)
	lpsnr = snr(org,lpimage)
	print("This is the snr for the lpdn")
	print(lpsnr);print(j+1)

#testsnr for wndn
wnimage = wndn(sig)
wnsnr = snr(org,wnimage)
print("This is the snr for the wndn")
print(wnsnr)

#testsnr for mvdn
for k in range(4):
	mvimage = mvdn(sig,rg=k+1)
	mvsnr = snr(org,mvimage)
	print("This is the snr for the mvdn")
	print(mvsnr);print(k+1)

#testsnr for wldn1
for i in range(30):
	wlimage1 = wldn1(sig,k=i)
	wlsnr1 = snr(org,wlimage1)
	print("This is the snr for the wldn1")
	print(wlsnr1);print(i+1)

#testsnr for wldn2
wls = pywt.wavelist()[0:15]+pywt.wavelist()[24:80]+[pywt.wavelist()[89],]
wls = wls + pywt.wavelist()[92:107]+pywt.wavelist()[108:]
max_num = 0
for j in range(len(wls)):
	for i in range(5):
		wlimage2 = wldn2(sig,rat=i/10.,wav=wls[j])
		wlsnr2 = snr(org,wlimage2)
		if (wlsnr2 > max_num):
			max_num = wlsnr2
			print("This is the snr for the ");print(wls[j])
			print(wlsnr2);print(i/10.)
