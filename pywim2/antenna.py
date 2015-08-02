# -*- coding: utf-8 -*-
"""
"""

from __future__ import division, absolute_import

import numpy as np

class Antenna:
    """Antenna object
    Parameters
    ----------
    num_elements : integer number larger than 0
    uniform_distance : nominal distance between elements, the unit is meter.

    See Also
    --------
    pywim2.antenna.ULA 

    """

    def __init__(self):
        # unit: meter
        self.num_elements = 1
        self.uniform_distance = 0

class ULA(Antenna):
    def __init__(self):
        pass
    
    def field_pattern(self, angle):
        return np.array( (1, 1) )








