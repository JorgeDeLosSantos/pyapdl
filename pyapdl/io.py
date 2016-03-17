# -*- coding: utf-8 -*-
from geometry import *

class Script(object):
    def __init__(self):
       self.__code = []
        
    def append(self,_str):
        self.__code.append(_str+"\n")
        
    def save(self,filename):
        f = open(filename, "w")
        f.writelines(self.__code)
        f.close()
        

if __name__ == '__main__':
    pass
    
