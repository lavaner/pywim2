from __future__ import division, absolute_import, print_function

import unittest
import numpy as np
from numpy.testing import *

import pywim2
from pywim2 import channel
import mock
from mock import patch

class TestChannelFilter(unittest.TestCase):

    def test_multipath(self):
        model = channel.Model()
        input = np.ones((1,10))

        coef = np.zeros((1,1,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        mock_gen_coef = mock.Mock(return_value=coef)
        with mock.patch('pywim2.channel.Model.gen_coef', mock_gen_coef):
            delay = [0,1,2]
            output = model.filter(input, delay)
            assert_array_equal(output,
                               np.array(((1,3,6,6,6,6,6,6,6,6),)))

        input = np.array(((1,1,1,1,1,1,1,1,1,1),
                          (2,2,2,2,2,2,2,2,2,2)))
        coef = np.zeros((2,1,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        coef[1,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        mock_gen_coef = mock.Mock(return_value=coef)
        with mock.patch('pywim2.channel.Model.gen_coef', mock_gen_coef):
            output = model.filter(input, delay)
            assert_array_equal(output,
                               np.array(((3,9,18,18,18,18,18,18,18,18),)))


        input = np.ones((1,10))
        coef = np.zeros((1,2,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        coef[0,1,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        mock_gen_coef = mock.Mock(return_value=coef)
        with mock.patch('pywim2.channel.Model.gen_coef', mock_gen_coef):
            output = model.filter(input, delay)
            assert_array_equal(output,
                               np.array(((1,3,6,6,6,6,6,6,6,6),
                                         (1,3,6,6,6,6,6,6,6,6))))
        
    def test_multiantenna(self):
        pass

class TestGenerateCoef(TestCase):

    @patch('pywim2.antenna.ULA')
    @patch('pywim2.channel.ChannelState')
    def test_fading(self, antenna, state):
        mock_cluster_state = mock.Mock('pywim2.channel.ClusterState')
        mock_cluster_state.num_rays = 1
        mock_cluster_state.ray_phases = np.zeros((1, 2))
        mock_cluster_state.polar_phases = np.zeros((1,4))
        mock_cluster_state.XPR = np.zeros((1))
        mock_cluster_state.theta_v = 0
        mock_cluster_state.v = 0
        mock_cluster_state.lambda_0 = 1

        state.cluster.return_value = mock_cluster_state
        antenna.field_pattern.return_value = np.array((1,1))
        antenna.uniform_distance = 0
        
        model = channel.Model()
        model.tx_antenna = antenna
        model.rx_antenna = antenna
        model.state = state
        
        coef = model.gen_fading(state.cluster(0), 1)

        assert_array_equal( coef, np.array((2.+0.j)) )

    @patch('pywim2.antenna.Antenna')
    @patch('pywim2.antenna.Antenna')
    @patch('pywim2.channel.ChannelState')    
    @patch('pywim2.channel.Model.gen_fading')
    def test_generate_coef(self, fading, state, tx_antenna, rx_antenna):
        fading.side_effect = (np.array((1,1,1,1)),
                              np.array((2,2,2,2)),
                              np.array((3,3,3,3)))

        tx_antenna.num_elements = 1
        rx_antenna.num_elements = 1
        state.num_paths = 3
        
        channel = pywim2.channel.Model()
        channel.tx_antenna = tx_antenna
        channel.rx_antenna = rx_antenna
        channel.state = state
        coef = channel.gen_coef(4)
        assert_array_equal( coef, np.array([[[[1,1,1,1],
                                              [2,2,2,2],
                                              [3,3,3,3]]]]))
        
if __name__ == '__main__':
    unittest.main()
    






