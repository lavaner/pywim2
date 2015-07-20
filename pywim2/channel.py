# -*- coding: utf-8 -*-
"""
"""

from __future__ import division, absolute_import

import numpy as np
from numpy import matlib

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
        self.inital_state = 0
        
    def filter(self, input, coef=1, delay=0):
        """Filter the input signal with specified model

        Parameters
        ----------
        input : 2-dimensional array of int Shape of 
            tx antenna element x number of samples
        
        See Also 
        --------

        Notes
        -----

        Examples
        --------
        """

        num_tx_ele, num_rx_ele, num_path, num_sample = coef.shape
        
        output = np.zeros((num_rx_ele, num_sample))

        delay_buffer = np.zeros((num_path, num_sample+np.max(delay)))
        for s in range(num_rx_ele):
            cluster_buffer = np.zeros((num_tx_ele, num_sample))

            for u in range(num_tx_ele):
                input_temp = matlib.repmat(input[u,:], num_path, 1)

                coef_matrix = coef[u,s,:,:]
                
                # multiple coef
                output_temp = input_temp*coef_matrix
      
                # delay
                for p in range(num_path):
                    delay_buffer[p, 
                                 delay[p]:delay[p]+num_sample] = output_temp[p, :]        

                cluster_buffer[u, :] = delay_buffer[:,:num_sample].sum(0) 

            # multipath combine
            output[s, :] = cluster_buffer.sum(0)

        return output
    
    def reset(self):
        """
        
        """
        pass

    def _generate_coefficient(self):
        pass

    def _generate_path_delays(self):
        pass

