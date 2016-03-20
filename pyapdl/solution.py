# -*- coding: utf-8 -*-

def sol():
    """
    Solution module
    """
    return "/SOLU"

def load_step_solve(n1,n2,inc=1):
    """
    Solve from load step n1 to n2
    """
    _lss = "LSSOLVE,%g,%g,%g"%(n1,n2,inc)
    return _lss
    
def solve():
    """
    Solve
    """
    return "SOLVE"

if __name__ == '__main__':
    print load_step_solve(1,10,1)
    
