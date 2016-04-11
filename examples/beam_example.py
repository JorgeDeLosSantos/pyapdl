# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.pardir)
from pyapdl import *

s = Script()

s.append("/PREP7")
# Create BEAM188 Elements
s.append(create_element(1,"BEAM188"))
# Keypoints
kps = {1:(0,0,0),
       2:(0.5,0,0),
       3:(1,0,0)}
for kp in kps:
    s.append(create_keypoint(kp,kps[kp]))
# Create lines. 1->2 & 2->3
s.append(create_line(1,2))
s.append(create_line(2,3))
# Create material
s.append(create_material(1,E=200e9,nu=0.3,density=7850))
# Section
s.append(create_beam_section(1,"_b1",ISection(0.05,0.05,0.05,0.01,0.01,0.01)))
# Mesh line
s.append(mesh_line(1))
s.append(mesh_line(2))
# Numbering nodes
s.append(numbering_nodes())
s.append(sol())
s.append(constraint_node(1))
s.append(load_node(5,fy=-1000))

s.preview()
s.save(r"outs/beam_example.txt")
