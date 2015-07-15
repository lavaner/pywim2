# -*- coding: utf-8 -*-
"""
"""

import numpy as np

class LargeScaleParameter:
    # Delay spread and distribution
    # Angle of Departure spread and distribution
    # Angle of Arrival Spread and distribution
    # Shadow Fading standard deviation
    # Ricean K-factor

    def __init__(self):
        pass


class SupportParameter:
    # Scaling parameter for Delay distribution
    # Cross-polarisation power ratios
    # Number of clusters
    # Cluster Angle Spread of Departure
    # Cluster Angle Spread of Arrival
    # Per Cluster Shadowing
    # Auto-correlations of the LS parameters
    # Cross-corelations of the LS parameters
    # Number of rays per cluster
    pass



class CDLModel:
    pass

class Antenna:
    pass

class Location:
    def __init__(x=0,y=0,z=0):
        x,y,x = 0,0,0


class BS:
    def __init__(self):
        pass

class MS:
    def __init__(self):
        pass

class ChannelModel:

    def __init__(self):
        self.Scenario
        self.bs
        self.ms
    
    def set_scenario(self, val):
        self.scenario = val

    def set_num_BS():
        pass

    def set_num_MS():
        pass
    
    
    def _generate_coefficient(self):
        pass

    def _generate_LSP(self):
        # Assign the propagation condition, Table 4-7
        for link in links:
            link.is_los_cond = self.scenario.is_los_cond(link.Distance)
        
        # calculate the path loss, Table 4-4
        for link in links:
            link.path_loss = self.scenario
        
        # genearate the correlated large scale parameter, Section 3.2.1
        for link in links:
            pass

    def _generate_SSP(self):
        pass

        
class Model:
    def __init__(self):
        self.state = 0
        
    def filter(self, input):

        coef_matrix = np.matrix([[1,1],[1,1]])
        input = np.matrix(np.ones([2,10]))
        output = np.matrix(np.zeros([2,10]))
        for i in range(input.shape[1]):
            output[::,i] = coef_matrix*input[::,i]
        
        return output



