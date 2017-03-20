import galsim
import math
import numpy
import matplotlib.pyplot as plt
random_seed=553728
sky_level=1.e4
pixel_scale=0.28
nx=64
ny=64
gal_flux_min=1.e4
gal_flux_max=1.e5
gal_hlr_min=0.3
gal_hlr_max=1.3
gal_e_min=0.
gal_e_max=0.8
psf_fwhm=[1.5,0.7,0.6,0.5]
psf_beta=[2.4,2.5,2.3,1.5]
gsparams=galsim.GSParams(folding_threshold=1.e-2,maxk_threshold=2.e-3,\
                         xvalue_accuracy=1.e-4,kvalue_accuracy=1.e-4,\
                         shoot_accuracy=1.e-4,minimum_fft_size=64)
psf1=galsim.Moffat(fwhm=psf_fwhm[0],beta=psf_beta[0],gsparams=gsparams) #to be continue
gal1=galsim.Gaussian(half_light_radius=1,gsparams=gsparams) #to be continue
psf=psf1
k=0
rng=galsim.UniformDeviate(random_seed+k+1)
flux=rng()*(gal_flux_max-gal_flux_min)+gal_flux_min
this_gal=gal1.withFlux(flux)
hlr=rng()*(gal_hlr_max-gal_hlr_min)+gal_hlr_min
this_gal=this_gal.dilate(hlr)
beta_ellip=rng()*2*math.pi*galsim.radians
ellip=rng()*(gal_e_max-gal_e_min)+gal_e_min
gal_shape=galsim.Shear(e=ellip,beta=beta_ellip)
this_gal=this_gal.shear(gal_shape)
final=galsim.Convolve([this_gal,psf])

image=galsim.ImageF(2*nx+2,ny,scale=pixel_scale)

fft_image=image[galsim.BoundsI(1,nx,1,ny)]

phot_image=image[galsim.BoundsI(nx+3,2*nx+2,1,ny)]
final.drawImage(fft_image,method='fft')

sky_level_pixel=sky_level*pixel_scale**2

fft_image.addNoise(galsim.PoissonNoise(rng,sky_level=sky_level_pixel))
rng=galsim.UniformDeviate(random_seed+k+1)
rng();rng();rng();rng();
final.drawImage(phot_image,method='phot',max_extra_noise=sky_level_pixel/100,\
                rng=rng)
pd=galsim.PoissonDeviate(rng,mean=sky_level_pixel)
phot_image.addNoise(galsim.DeviateNoise(pd))
phot_image -= sky_level_pixel

image0=galsim.ImageF(2*nx+2,ny,scale=pixel_scale)

fft_image0=image0[galsim.BoundsI(1,nx,1,ny)]

phot_image0=image0[galsim.BoundsI(nx+3,2*nx+2,1,ny)]
final.drawImage(fft_image0,method='fft')

#fft_image.addNoise(galsim.PoissonNoise(rng,sky_level=sky_level_pixel))
#rng=galsim.UniformDeviate(random_seed+k+1)
#rng();rng();rng();rng();
final.drawImage(phot_image0,method='phot',max_extra_noise=sky_level_pixel/100)

imaged=image-image0
