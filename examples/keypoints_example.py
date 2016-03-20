# -*- coding: utf-8 -*-
import sys
sys.path.append(r"C:\Users\User\Desktop\LABPro\PX1604 - PyAPDL\pyapdl")
from pyapdl.modeling import *
from pyapdl.io import *

s = Script()
kps = {1:(0,0,0),
       2:(1,0,0),
       3:(1,1,0),
       4:(0,1,0)}

for kp in kps:
    s.append(create_keypoint(kp, kps[kp]))

s.save(r"outs/keypoints_example.txt")
