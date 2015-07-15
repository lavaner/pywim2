# -*- coding: utf-8 -*-


import numpy as np

class Scenario:
    def is_los_cond(self, d):
        return np.random() > self._prob_los(d)
        
    
    def _prob_los(self, d):
        """
        Table 4-7 Line of sight probabilities
        """
        pass


    def _gen_delays(self):
        """
        Step 5
        """
        tau_tmp = []
        for i in range(N):
            x = random()
            tau_tmp_ele = -r_tau*sigma_tau*log(x)
            tau_tmp.append(tau_tmp_ele)

        tau = (tau_tmp - min(tau_tmp)).sort()

        D = 0.7705-0.0433*K+0.0002*K**2+0.000017*K**3
        tau_LOS = tau / D

        return tau, tau_LOS

    def _gen_cluter_power(self):
        """
        Step 6
        """
        P_tmp = exp(-tau*(r_tau - 1)/(r_tau*sigma_tau))*10**(-Z/10)
        P_tmp = exp(-tau/sigma_tau)*10**(-Z/10)

        P = P_tmp / sum(P_tmp)

        return P

    def _gen_azimuth(self):
        """
        Step 7a
        """

        for n in range(20):
            phi[n] = 2*sigma_AOA*np.sqrt(log(P[n]/np.max(P))) / C
            sigma_AOA = sigma_phi / 1.4
            
        C_TABLE = [0.779, 0.860, 1.018, 1.090, 1.123,
                       1.146, 1.190, 1.211, 1.226, 1.289]
        C_LOS = C*(1.1035 - 0.028*K-0.002*K**2+0.0001*K**3)

        for n in range(20):
            phi[n] = X[n]*phi[n]+Y[n]+phi_LOS

        RayOffset_TABLE = [+0.0447,-0.0447,
                           +0.1413,-0.1413,
                           +0.2492,-0.2492,
                           +0.3715,-0.3715,
                           +0.5219,-0.5219,
                           +0.6797,-0.6797,
                           +0.8844,-0.8844,
                           +1.1481,-1.1481,
                           +1.5195,-1.5195,
                           +2.1551,-2.1551]
                    
        return phi

    def _gen_elevation(self):
        """
        Step 7b
        """

        pass

    def _random_couple(self, departure, arrival):
        """
        Step 8 Random coupling of rays within clusters
        """
        
        return 

    def _gen_XPR(self):
        """
        Step 9
        """
        for m in range(M):
            for n in range(N):
                X = mu + siama*np.randn()        
                kappa[m][n] = 10**(X/10)

        return kappa
    
    
    def _gen_coeffiecient(self):
        """
        
        """
        for u :
            for s :
                for n:
                    for m:
                        
                        for t:
                            fading_m_tmp = exp(j*d[s]*2*pi*lambda**-1*sin(phi[n, m]))*\\
                                           exp(j*d[u]*2*pi*lambda**-1*sin(phi[n, m]))*\\
                                           exp(j*2*pi*v[n, m]*t)
                        fading_m = np.matrix(F(phi[n, m]), F(phi[n, m])).tranpose() * \\
                                   np.matrix(np.exp(j*phi_hh[n,m] np.sqrt(k[n,m]) * exp(1j*phi_vh[n,m]) \\
                                                    np.sqrt(k[n,m])*exp(1j*phi_hv[n,m] exp(1j*phi_hh(n,m)) * \\
                                   np.matrix(F(phi[n, m]), F(phi[n, m]))
                        fading = fading + fading_m
    
class A1(Scenario):
    """
    Indoor Office
    """
    
    PARAMS_LOS = ((-7.42, 0.27), (1.64, 0.31), (1.65, 0.26), (3), (7, 6),
                  (0.7, 0.8,-0.5,-0.5,-0.6,0.6,-0.6,-0.6,-0.6,0.4),
                  (@exp), (@wrapped_gaussian), (3), (11, 4), (12), (20),
                  (5), (5), (6), (7), (6), (2), (6), (6))
    PARAMS_NLOS = ((-7.60, 0.19), (1.73, 0.23), (1.69, 0.14), (4), (NaN, NaN),
                  (-0.1, 0.3, -0.4, 0, -0.5, -0.3, NaN, NaN, NaN, NaN),
                  (@exp), (@wrapped_gaussian), (2.4), (10, 4), (16), (20),
                  (5), (5), (3), (4), (5), (3), (4), (NaN))
    
    def __init__(self):
        self.num_wall = 0
        self.sub_type = 'Corridor-to-Room' # Corridor-to-Room/Room-to-Room
        self.wall_style = 'light' #light/heavy
    
    def _path_loss_par(self):
        if self.is_los_cond():
            A, B, C, X = 18.7, 46.8, 20, 0
            sigma = 3
        elif self.sub_type == 'Corridor-to-Room':
            A, B, C = 36.8, 43.8, 20
            simga = 4
            if self.wall_style == 'light':
                X = 5*(self.num_wall - 1)
            elif self.wall_style == 'heavy':
                X = 12*(self.num_wall - 1)
            else:
                raise WIM2_Error_UnreconizedParameter()
            
        elif: self.sub_type == 'Room-to-Room':
            A, B, C = 20, 46.4, 20
            if self.wall_style == 'light':
                X = 5*self.num_wall
                sigma = 6
            elif self.wall_style == 'heavy':
                X = 12*self.num_wall
                sigma = 8
            else:
                raise WIM2_Error_UnreconizedParameter()
                
        else:
            raise WIM2_Error_UnreconizedParameter()
            
        return A, B, C, X, sigma
            

    
    def _prob_los(self, d):
        if d <= 2.5:
            plos = 1
        else:
            plos = 1-0.9*(1-(1.24-0.61*log10(d))^3)^(1/3)

        return plos

class A2(Scenario):
    """
    Indoor to outdoor
    """
    PARAMS_NLOS = (([-7.39, -6.62], [0.36, 0.32]), (1.76, 0.16), (1.25, 0.42), (7), (NaN, NaN),
                  (-0.4, 0.4, 0.2, 0, -0.5, 0, NaN, NaN, NaN, NaN),
                  (@exp), (@wrapped_gaussian), (2.2), (9, 11), (12), (20),
                   (8), (5), (4), ([21, 10]), ([15, 11]), ([35, 17]), ([14, 7]), (NaN))
    
    
class B1(Scenario):
    """
    Urban micro-cell
    """

    PARAMS_LOS = ((-7.44, 0.25), (0.40, 0.37), (1.40, 0.20),  (3), (9, 6),
                  (0.5, 0.8, -0.5, -0.5, -0.4, 0.4, -0.3, -0.3, -0.7, 0.5),
                  (@exp), (@wrapped_gaussian), (3.2), (9, 3), (8), (20),
                   (3), (18), (3), (9), (13), (12), (14), (10))
    PARAMS_NLOS = ((-7.12, 0.12), (1.19, 0.21), (1.55, 0.20), (4), (NaN, NaN),
                  (0.2, 0.4, -0.4, 0, -0.7, 0.1, NaN, NaN, NaN, NaN),
                  (@uniform), (@wrapped_gaussian), (NaN), (8, 3), (16), (20),
                   (10), (22), (3), (8), (10), (9), (12), (NaN))
    
    def _prob_los(self, d):
        plos = min(18/d, 1)*(1-exp(-d/36))+exp(-d/36)

        return plos

class B2(Scenario):
    """
    Bad Urban micro-cell
    """
    pass

class B3(Scenario):
    """
    Indoor hotspot
    """
    
    PARAMS_LOS = ((-7.53, 0.12), (1.22, 0.18), (1.58, 0.23),  (3), (2, 3),
                  (-0.3, -0.4, -0.2, 0.3, -0.1, 0.3, 0.2, -0.1, -0.3, 0.6),
                  (@exp), (@wrapped_gaussian), (1.9), (9, 4), (10), (20),
                   (5), (5), (3), (3), (1), (2), (3), (1))
    PARAMS_NLOS = ((-7.41, 0.13), (1.05, 0.22), (1.7, 0.1), (4), (NaN, NaN),
                  (-0.1, 0, 0.2, -0.3, -0.2, -0.3, NaN, NaN, NaN, NaN),
                  (@uniform), (@wrapped_gaussian), (1.6), (6, 3), (15), (20),
                   (6), (13), (3), (1), (0.5), (0.5), (3), (NaN))    
    
    def _prob_los(self, d):
        if d <= 10:
            plos = 1
        else:
            plos = exp(-(d-10)/45)

        return plos

class B4(Scenario):
    """
    Outdoor to indoor
    """
    pass
    
class B5(Scenario):
    """
    Stationary Feeder
    """
    pass

class C1(Scenario):
    """
    Suburban macro-cell
    """

    PARAMS_LOS = ((-7.23, 0.49), (0.78, 0.12), (1.48, 0.20),  ([4,6]), (9, 7),
                  (0.2, 0.8, -0.5, -0.5, -0.6, 0.1, 0.2, -0.2, -0.2, 0),
                  (@exp), (@wrapped_gaussian), (2.4), (8, 4), (15), (20),
                   (5), (5), (3), (6), (15), (20), (40), (10))
    PARAMS_NLOS = ((-7.12, 0.33), (0.90, 0.36), (1.65, 0.30), (8), (NaN, NaN),
                  (0.3, 0.7, -0.3, -0.4, -0.4, 0.3, NaN, NaN, NaN, NaN),
                  (@exp), (@wrapped_gaussian), (1.5), (4, 3), (14), (20),
                   (2), (10), (3), (40), (30), (30), (50), (NaN))    

    def _prob_los(self, d):
        return exp(-d/200)

class C2(Scenario):
    """
    Urban macro-cell
    """
    def _prob_los(self, d):
        return min(18/d, 1)*(1-exp(-d/63)) + exp(-d / 63)

class C3(Scenario):
    """
    Bad urban macro-cell
    """
    pass

class C4(Scenario):
    """
    Urban macro outdoor to indoor
    """
    pass

class D1(Scenario):
    """
    Rural macro-cell
    """
    def _prob_los(self, d):
        return exp(-d/1000)

class D2:
    """
    Moving networks
    """










