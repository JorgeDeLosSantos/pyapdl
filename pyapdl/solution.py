# -*- coding: utf-8 -*-

def sol():
    return "/SOLU"

def load_step_solve(n1,n2,inc=1):
    _lss = "LSSOLVE,%g,%g,%g"%(n1,n2,inc)
    return _lss
    
def solve():
    return "SOLVE"

if __name__ == '__main__':
    print load_step_solve(1,10,1)
    
