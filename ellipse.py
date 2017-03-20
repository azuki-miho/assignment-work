import numpy as np

def elli(psfimage):
	nx,ny  = psfimage.shape[0],psfimage.shape[1]
	x,y    = np.mgrid[:nx,:ny]
	m00    = np.sum(psfimage)
	x0     = np.sum(x*psfimage)/m00
	y0     = np.sum(y*psfimage)/m00
	mxy  =np.sum((y-y0)*(x-x0)*psfimage)/m00
 	mxx  =np.sum((x-x0)*(x-x0)*psfimage)/m00
	myy  =np.sum((y-y0)*(y-y0)*psfimage)/m00

	itr  =10
	for i in range(itr):
		detM =mxx*myy-mxy*mxy
		mxx  =mxx/detM
		myy  =myy/detM
		mxy  =-mxy/detM

		w    =(x-x0)*(x-x0)*mxx+2.0*(x-x0)*(y-y0)*mxy+(y-y0)*(y-y0)*myy
		w    =np.exp(-0.5*w)
		m00  =np.sum(w*psfimage)
		x0   =np.sum(x*w*psfimage)/m00
		y0   =np.sum(y*w*psfimage)/m00
		mxy  =np.sum((y-y0)*(x-x0)*w*psfimage)
		mxx  =np.sum((x-x0)*(x-x0)*w*psfimage)
		myy  =np.sum((y-y0)*(y-y0)*w*psfimage)


	e1 = (mxx - myy) / (mxx + myy)
	e2 = (2 * mxy) / (mxx + myy)
	return (e1,e2)
