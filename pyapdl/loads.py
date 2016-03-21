# -*- coding: utf-8 -*-
import numpy as np

def constraint_node(node,**bc):
    _bc = ""
    if not bc:
        _bc += "D,%s,ALL,,"%(node)
    else:
        for constraint in bc:
            _bc += ("D,%s,%s,%g\n"%(node,constraint,bc[constraint])).upper()
    return _bc



def load_node(node,**load):
    _load = ""
    if not load:
        pass
    else:
        for ld in load:
            _load += ("F,%s,%s,%g\n"%(node,ld,load[ld])).upper()
    return _load

    
def load_line(line,**load):
    pass
    
def load_area(area,**load):
    pass



if __name__ == '__main__':
    #print constraint_node(1,ux=0,uy=0)
    print load_node(5,fy=-1000)
