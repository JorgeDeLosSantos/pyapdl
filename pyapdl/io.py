# -*- coding: utf-8 -*-

class Script(object):
    """
    Script class for I/O operations
    """
    def __init__(self,name="Script 01"):
        self.name = name
        self.__code = []
        
    def append(self,_str):
        """
        Append lines to script
        """
        if isinstance(_str,tuple) or isinstance(_str,list):
            for cd in _str:
                self.__code.append("%s\n"%(cd))
        else:
            self.__code.append("%s\n"%(_str))
    
    def preview(self):
        """
        Get script preview
        """
        print("Current preview for <%s>:\n\n%s"%(self.name,self.__str__()))
    
    def save(self,filename):
        """
        Save script lines to filename
        """    
        f = open(filename, "w")
        f.writelines(self.__code)
        f.close()
        print("Saved script to %s\n"%(filename))
        
    def __str__(self):
        return "".join(self.__code)


if __name__ == '__main__':
    pass
    
