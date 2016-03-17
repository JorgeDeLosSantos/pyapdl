# PyAPDL

Programming in ANSYS Parametric Design Language (APDL) using Python


### Mini Example

1. Creating two keypoint from a list of coordinates.

```python
# -*- coding: utf-8 -*-
from pyapdl.geometry import *
from pyapdl.io import *

s = Script()
coords = [(0,0,0),(0,1,0)]
for k,crd in enumerate(coords):
    s.append(create_keypoint(k+1,crd))

s.save("example.txt")
```

### Instalation

Using git to clone this repository (or download zip):

```
$ git clone https://github.com/JorgeDeLosSantos/pyapdl.git
```

and run the `setup.py`:

```
>> python setup.py install
```

### About...

```
Author: Pedro Jorge De Los Santos
E-mail: delossantosmfq@gmail.com
```