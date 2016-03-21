# -*- coding: utf-8 -*-
class Section(object):
    def __init__(self):
        pass

class RectangleSection(Section):
    def __init__(self,b,h):
        Section.__init__(self)
        self.b = b
        self.h = h
        self.type = "RECT"
    
    def get_data(self):
        self.data = (self.b,self.h,2,2)
        return (len(self.data)*"%s,")%self.data
        
class ISection(Section):
    def __init__(self,w1,w2,w3,t1,t2,t3):
        Section.__init__(self)
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.type = "I"
    
    def get_data(self):
        self.data = (self.w1, self.w2, self.w3, self.t1, self.t2, self.t3)
        return (len(self.data)*"%s,")%self.data
    

def create_beam_section(sid,sname,stype):
    _bs = "SECTYPE,%s,BEAM,%s,%s,0"%(sid,stype.type,sname) # Beam section
    _bd = "SECDATA,%s"%(stype.get_data())
    return "\n".join([_bs,_bd])

    
if __name__ == '__main__':
    print create_beam_section(1,"_b1",RectangleSection(0.2,0.2))
