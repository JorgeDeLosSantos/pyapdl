# -*- coding: utf-8 -*-
import numpy as np

def create_keypoint(n,*args):
    """
    Parameters:
    -----------
    n : int
        Keypoint number
    *args: tuple, int, float
        *args must be a tuple of (x,y,z) coordinates or x, y and z 
        coordinates as arguments.
        
    ::
    
        # Example
        kp1 = 1
        kp2 = 2
        create_keypoint(kp1,(0,0,0)) # x,y,z as tuple
        create_keypoint(kp2,1,1,1) # x,y,z as arguments
    """
    if len(args)==1 and isinstance(args[0],tuple):
        x,y,z = args[0][0],args[0][1],args[0][2]
    else:
        x,y,z = args[0], args[1], args[2]
    _kp = "K,%g,%g,%g,%g"%(n,x,y,z)
    return _kp

def create_node(n,*args):
    """
    Parameters:
    -----------
    n : int
        Node number
    *args: tuple, int, float
        *args must be a tuple of (x,y,z) coordinates or x, y and z 
        coordinates as arguments.
        
    ::
    
        # Example
        node1 = 1
        node2 = 2
        create_node(node1,(0,0,0)) # x,y,z as tuple
        create_node(node2,1,1,1) # x,y,z as arguments
    """
    if len(args)==1 and isinstance(args[0],tuple):
        x,y,z = args[0][0],args[0][1],args[0][2]
    else:
        x,y,z = args[0], args[1], args[2]
    _nd = "N,%g,%g,%g,%g"%(n,x,y,z)
    return _nd
    
def create_line(kp1,kp2):
    """
    Parameters:
    -----------
    kp1 : int
        First keypoint
    kp2 : int
        Second keypoint
    """
    _ln = "L,%g,%g"%(kp1,kp2)
    return _ln

if __name__ == '__main__':
    print create_keypoint(1,0,0,0)
    print create_node(1,2.0,1,20)
    print create_line(1,10)
