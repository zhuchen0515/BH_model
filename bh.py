## bh.py

"""
Calculate the heating rate with different methods

@Author: ZhuChen

Date: Nov.3, 2016
"""

import numpy as np
from const import *

class ClassBH(object):
     def __init__(self):
          self.A = 0.25; self.p = 1.0; self.q = 1.0
          self.a = 9.18; self.b = 1.99
          self.c = 0.31; self.d = 4.38
          self.f = 0.066

     def __del__(self):
          pass

     ##The fitting parameters of sig1, re and mstar
     def pass_param_lsig1(self,A,p,q):
          self.A = A  ##fitting slope of sig1,re and mstar relation
          self.p = p  ##slope of re
          self.q = q  ##slope of mstar

     def v_lsig1(self,lm_sz,lr_z):
          lsig1 = np.log10(self.A)+self.q*lm_sz-self.p*lr_z
          return lsig1

     ## Ref. Fang et al. 2013 plot
     ## log sig1(mass density) vs log Sig1(velocity dispersion) relation fitting parameters
     def pass_param_lvsig1(self,a,b):
          self.a = a  ##intercept
          self.b = b  ##slope

     def v_lvsig1(self,lm_sz,lr_z):
          lsig1 = self.v_lsig1(lm_sz,lr_z)
          lvsig1 = 2+(lsig1 -self.a)/self.b
          return lvsig1

     ## Ref. Wache et al. 2012b, p2
     ## log Sig_1(velocity despersion), log Sig_e and Reff relation fitting parameters
     def pass_param_lvsige(self,f):
          self.f = f ##slope of Re

     def v_lvsige(self,lm_sz,lr_z):
          lvsig1 = self.v_lvsig1(lm_sz,lr_z)
          lvsige = lvsig1-self.f*lr_z
          return lvsige

     ## Ref. Kormendy and Ho
     ## black hole mass and sig_e relation fitting parameters
     def pass_param_lmbh(self,c,d):
          self.c = c  ##intercept
          self.d = d  ##slope

     def v_lmbh(self,lm_sz,lr_z):
          lvsige = self.v_lvsige(lm_sz,lr_z)
          lmbh = np.log10(self.c)+self.d*(lvsige-np.log10(200.))+9.
          return lmbh


