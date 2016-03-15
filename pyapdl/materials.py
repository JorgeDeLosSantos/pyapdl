# -*- coding: utf-8 -*-
import numpy as np

class Material(object):
    def __init__(self,name,**props):
        """
        Create a material class
        
        Properties
        ----------
        E        : int,float
            Young modulus
        nu       : int,float
            Poisson's ratio
        density  : int,float
            Density
        """
        self.name = name
        if props.has_key("E"): self.__E = props["E"]
        if props.has_key("nu"): self.__nu = props["nu"]
        if props.has_key("density"): self.__density = props["density"]
    
    @property
    def nu(self):
        return self.__nu
        
    @nu.setter
    def nu(self,val):
        self.__nu = val
    
    @property
    def E(self):
        return self.__E
    
    @E.setter
    def E(self,val):
        self.__E = val
        
    @property
    def density(self):
        return self.__density
    
    @density.setter
    def density(self,val):
        self.__density = val
        
    def toANSYS(self,number):
        E_str = "MP,EX,%g,%g"%(number,self.E)
        nu_str = "MP,NUXY,%g,%g"%(number,self.nu)
        density_str = "MP,DENS,%g,%g"%(number,self.density)
        return "\n".join([E_str,nu_str,density_str])
        

if __name__ == '__main__':
    pass
