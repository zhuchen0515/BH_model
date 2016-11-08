## size.py

"""
Calculate the heating rate with different methods

@Author: ZhuChen

Date: Nov.3, 2016
"""

from __init__ import *
from random import randint

## Class about the galaxy size
class ClassReff(object):
     def __init__(self):
          self.slope = 0.2

     def __del__(self):
          pass

     ## get the initial re for galaxy at logmass=9 
     ## From van der Wel et al. 2013
     def get_lr9(self,lr9,elr9=0.2,num=15000):
          temp = np.random.normal(lr9,elr9,num)
          ran = randint(0,num-1)
          lr_9 = temp[ran]
          while lr_9 < -0.1 or lr_9 > 1.5:  
               temp = np.random.normal(lr9,elr9,num)
               ran = randint(0,num-1)
               lr_9 = temp[ran]     
          return lr_9
     
     ## if rand=True will use the scatter from the paper to generate re randomly
     ## if rand= False will use the re at the fitting line
     def v_lr9(self,z,rand=False):
          if z>=2.5:
               lr9 = 0.51-0.18*1.699
               elr9 = 0.19
          elif z>=2.0 and z<2.5:
               lr9 = 0.55-0.22*1.699
               elr9 = 0.19
          elif z>=1.5 and z<2.0:
               lr9 = 0.65-0.23*1.699
               elr9 = 0.18
          elif z>=1.0 and z<1.5:
               lr9 = 0.70-0.22*1.699
               elr9 = 0.17
          elif z>=0.5 and z<1.0:
               lr9 = 0.78-0.22*1.699
               elr9 = 0.16
          elif z<0.5:
               lr9 = 0.86-0.25*1.699
               elr9 = 0.16
          if rand==True:
               lr9 = self.get_lr9(lr9,elr9)
          else:
               lr9 = lr9
          return lr9

     ## pass the parameter of the relation between galaxy size and stellar mass
     def pass_param_lrz(self,slope):
          self.slope = slope     

     ##get the evolution of re
     def v_lrz(self,lm_sz,lr_9):
          lr_z = lr_9+self.slope*(lm_sz-9)
          return lr_z

