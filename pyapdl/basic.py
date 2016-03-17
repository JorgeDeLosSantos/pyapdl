# -*- coding: utf-8 -*-
import numpy as np

def comment(_str):
    return "!%s"%(_str)

def create_array(name,array):
    init_str = "*DIM,%s,ARRAY,%g\n"%(name,len(array))
    fill_str = "%s(1)=%s\n"%(name,",".join([str(k) for k in array]))
    return "%s%s"%(init_str,fill_str)



    
if __name__ == '__main__':
    print create_array("time",[1,2,3,2])
