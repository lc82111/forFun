# -*- coding: utf-8 -*-
# making gabor patch
# ref:http://www.icn.ucl.ac.uk/courses/MATLAB-Tutorials/Elliot_Freeman/html/gabor_tutorial.html
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

imSize = 100;                           # image size: n X n
lamda = 10;                             # wavelength (number of pixels per cycle)
theta = 15;                             # grating orientation
sigma = 10;                             # gaussian standard deviation in pixels
phase = .25;                            # phase (0 -> 1)
trim = .005;                            # trim off gaussian values smaller than this

X=np.asarray(range(1,imSize),dtype=float)

X0=(X/imSize) - 0.5                    #make X0 in (-0.5, 0,5)
sinX=np.sin(X0*2*np.pi)                #sin(-pi,pi)
plt.plot(X0*2*np.pi, sinX)

#改变频率
freq=imSize/lamda
Xf = X0 * freq * 2*np.pi
sinX2=np.sin(Xf)
plt.plot(X0*2*np.pi, sinX2)

#改变相位
phaseRad = (phase * 2* np.pi)
sinX3 = np.sin( Xf + phaseRad)
plt.plot(X0*2*np.pi, sinX3)

#Now make a 2D grating
#Start with a 2D ramp use meshgrid to make 2 matrices with ramp values across columns (Xm) or across rows (Ym) respectively
Xm,Ym = np.meshgrid(X0,X0)
tmp=np.concatenate((Xm,Ym),1)
plt.imshow(tmp,'jet')
plt.imshow(Xm+Ym, 'jet')

#Put 2D ramps through sine
Xf = Xm * freq * 2*np.pi
grating = np.sin( Xf + phaseRad)          # make 2D sinewave
plt.imshow(grating, 'Greys')

#Change orientation by adding Xm and Ym together in different proportions
thetaRad = (theta/360.0)* 2*np.pi # convert theta (orientation) to radians
Xt = Xm * np.cos(thetaRad)
Yt = Ym * np.sin(thetaRad)
XYt= Xt + Yt
XYf= XYt * freq * 2*np.pi
grating = np.sin(XYf + phaseRad)
plt.imshow(grating, 'Greys')

#make a gaussian mask
#1D
s = float(sigma) /imSize #gaussian width as fraction of imageSize
Xg = np.exp(-( (X0**2 * 1.0) / (2.0*s**2) ))
Xg = Xg / (s * np.sqrt(2.0*np.pi))
#Xg = np.normpdf(X0, 0, (20/imSize))
#Xg = Xg/Xg.max()
plt.plot(Xg)

#2D
gauss = np.exp( -(((Xm**2)+(Ym**2)) / (2.0* s**2)) )
p=plt.imshow(gauss, cmap=plt.cm.Greys_r, vmin=-0.5, vmax=1.)

#scipy.stats.norm.pdf(X0, 0, 0.1)
#def normpdf(x, mu, sigma):
#    u = (x-mu)/abs(sigma)
#    y = (1/(np.sqrt(2.0*np.pi)*abs(sigma)))*np.exp(-u*u/2.0)
#    return y
#x = np.arange(-5, 5, 0.1)
#y = np.arange(-5, 5, 0.1)
#xx, yy = np.meshgrid(x, y)
#z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
#h = plt.contourf(x,y,z)

