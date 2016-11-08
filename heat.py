## heat.py

"""
Calculate the heating rate with different methods

@Author: ZhuChen

Date: Nov.3, 2016
"""

import numpy as np
from const import *
from bh import ClassBH
from cool import ClassHaloP 

class ClassHeat(ClassBH,ClassHaloP):
     def __init__(self,omega_m=0.3,omega_l=0.7,omega_b=0.048,h0=0.7):
          ClassBH.__init__(self)
          ClassHaloP.__init__(self,omega_m=omega_m,omega_l=omega_l,omega_b=omega_b,h0=h0)
          self.eta = 0.1
          self.k_AGN = 6.0e-6
          self.fhot = 0.1

     def __del__(self):
          pass

     ##pass the parameters for black hole accretion rate rate calculation
     def pass_param_lmbh_acrate(self,k_AGN,fhot):
          self.k_AGN = k_AGN  ##Msun/yr  ##coefficient before BH accretion rate Hernques et al. 2015 Eq.S24
 	     
          self.fhot = fhot
     
     ##calculate the black hole accretion rate Msun/yr
     def v_lmbh_acrate(self,lm_sz,lm_hz,lr_z,z):
          lm_bh = self.v_lmbh(lm_sz,lr_z)
          lVvir = self.v_lVvir(lm_hz,z)
          lmbh_acrate = np.log10(self.k_AGN)+lm_bh-8+np.log10(self.fhot)+1+3*(lVvir-np.log10(200))
          return lmbh_acrate

     ##pass the parameter to calculate the mass heating rate
     def pass_param_olmheat(self,eta):
          self.eta = eta  ##coefficient before energy input rate Hernques et al 2015 Eq.S25

     ##calculate the old mass heating rate Msun/yr
     def v_lmheat_old(self,lm_sz,lm_hz,lr_z,z):
          lmbh_acrate = self.v_lmbh_acrate(lm_sz,lm_hz,lr_z,z)
          lVvir = self.v_lVvir(lm_hz,z)
          lm_heat = np.log10(2*self.eta)+lmbh_acrate+2*(np.log10(3.0e5)-lVvir)
          return lm_heat

     ##calculate the new mass heating rate Msun/yr
     def v_lmheat_new(self,lm_sz,lm_hz,lr_z,z):
          lVvir = self.v_lVvir(lm_hz,z)
          lsig1 = self.v_lsig1(lm_sz,lr_z)
          lm_heat = np.log10(2.36)-14+lm_sz*(0.2*(lsig1-3))-lr_z-2*lVvir+2*np.log10(3.0e5)
          return lm_heat

     
