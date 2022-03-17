#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:31:19 2022

@author: molierenguile-makao
"""

class facequadri:
    def __init__(self,larg,long,haut=None):
        self.lrg=larg
        self.log=long
        self.hat=haut
        
    def perimetre(self):
        if self.hat is None:
            return 2*(self.log+self.lrg)
        else:
            return 2*(self.log+self.lrg+self.hat)
        
    def volume(self):
        if self.hat is None :
            return self.lrg*self.log
        else:
            return self.lrg*self.log*self.hat