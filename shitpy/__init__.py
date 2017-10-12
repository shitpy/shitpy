from .dataTypes import *
from .dataStructures import *

import sys
if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    raise ImportError("Python Version 2.6 or above is required for SymPy.")

del sys