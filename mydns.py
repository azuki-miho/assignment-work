import numpy as np
from scipy.signal import wiener
from scipy import signal
import pywt
def lpdn(img,r=17):
	h,w=img.shape
	img2=np.fft.fft2(img)
	fshift=np.fft.fftshift(img2)
	st=fshift.copy()
	h,w=fshift.shape
	sh=h/2
	sw=w/2
	for i in range(h):
		for j in range(w):
			if ((sh-i)**2+(sw-j)**2)<=r**2:
				tmp=1
			else:
				tmp=0
			st[i,j]=tmp*fshift[i,j]
	sl=np.fft.ifftshift(st)
	img2d=np.fft.ifft2(sl)
	imgd=np.real(img2d)
	return imgd

def wndn(img):
	img2=wiener(img)
	return img2

def mvdn(img,R=1,rg=4):
	h,w=img.shape
	rt=np.zeros((h,w))
	for i in range(h):
		for j in range(w):
			if (i>=R and i<=h-1-R):
				if(j>=R and j<=w-1-R):
					arr=[]
					for m in range(2*R+1):
						for n in range(2*R+1):
							arr.append(img[i+m-R][j+n-R])
					arr.sort()
					val=np.mean(arr[2*(R**2)+2*R-rg:2*(R**2)+2*R+rg])
			else:
				ab=[]
				ab.append(abs(i))
				ab.append(abs(j))
				ab.append(abs(h-1-i))
				ab.append(abs(w-1-j))
				ab.sort()
				r=ab[0]
				arr=[]
				for m in range(2*r+1):
					for n in range(2*r+1):
						arr.append(img[i+m-r][j+n-r])
				arr.sort()
				val=arr[2*(r**2)+2*r]
			rt[i][j]=val
	return rt

def wldn1(img,k=2):
	h,w=img.shape
	rt=np.zeros((h,w))
	for i in range(h):
		temp=img[i]
		widths=np.arange(1,31)
		cwtmatr=signal.cwt(temp,signal.ricker,widths)
		rt[i]=cwtmatr[k-1]
	return rt

def wldn2(img,rat=0.0,wav="db31"):
	coeffs2 = pywt.dwt2(img,wav)
	ll,(lh,hl,hh) = coeffs2
	h,w = hh.shape
	for i in range(h):
		for j in range(w):
			lh[i][j] = rat*lh[i][j]
			hl[i][j] = rat*hl[i][j]
			hh[i][j] = rat*hh[i][j]
	coeffs2t = ll,(lh,hl,hh)
	rt = pywt.idwt2(coeffs2t,wav)
	return rt

def snr(image0,image1):
	h,w=image0.shape
	imagen=image1-image0
	sigp=0
	nsp=0
	for i in range(h):
		for j in range(w):
			sigp=sigp+(image0[i][j])**2
			nsp=nsp+(imagen[i][j])**2
	ratio=sigp/nsp
	return ratio
