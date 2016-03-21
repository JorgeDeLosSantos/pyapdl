# -*- coding: utf-8 -*-

def create_element(number,etype):
    """
    Create an element:
    
    Parameters
    ----------
    
    number : int
        Number of element
    etype  : str
        Element type
    
    ::
    
        # Example 
        create_element(1, "PLANE182") # -> ET,1,PLANE182
    """
    _el = "ET,%g,%s"%(number,etype)
    return _el
    

if __name__ == '__main__':
    pass
