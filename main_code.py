#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:28:50 2023

@author: personal
"""

import pandas as pd
import numpy as np
import pylab as pl
import sciris as sc
import covasim as cv
import covasim.parameters as cvp
from datetime import datetime
import datetime as dt
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib as plt
import datetime


cv.check_version('>=3.1.4')
cv.git_info('covasim_version3.json')

pl.close('all')

start_day = '2020-01-20'
end_day   = '2023-04-30'

# x is an unused variable other than to set the seed

# per_vac is one of (0,1,2,3,4,5,6,7,8,9,10) and corresponds to the percentage of adoelscents
# vaccinated (i.e. i=2 is 20% of adolescents vaccinated) except in the case of i=10 which 
# corresponds to the baseline scenario (approx 47% of those aged 12-15 and 60% for thoses 
# aged 16-17

# day_start is one of (0,1,2,3,4,5,6) and corresponds to the date which adolescent vaccination 
# is beginning with i2 = 0 starting vaccination for those aged 16-17 on 01/08/21 and for 
# those aged 12-15 on 29/08/21, then i2 = 1 starting 2 weeks after these dates, i2 = 2 
# starting 4 weeks after these dates and so on... with the exception of i2 = 6 which 
# corresponds to the actual adolescent vaccination start dates in the UK (16-17 23/08/21 
# and 12-15 20/09/21) 

# booster_ind is one of (0,1,2,3,4) where 0 is no booster vaccine at all, 1 is one 
# age-prioritised booster for all adults, 2 is an additional booster vaccine for those 
# aged over 75, 3 is an additional booster for those aged over 50 (the baseline scenario), 
# 4 is an additional booster vaccine for adolescents

# with_omicron is one of (0,1) where 0 indicates no omicron variants are introduced, and 
# 1 is with the omicron variants being introduced (the baseline scenario)

def create_sim(x,per_vac,day_start,booster_ind, with_omicron):

    start_day = '2020-01-20'
    end_day   = '2023-04-30'
    data_path = 'england_gov_data_trial.xlsx'

    # Set the parameters
    total_pop    = 55.98e6 # England population size
    pop_size     = 100e3 # Agent population size
    pop_scale    = int(total_pop/pop_size)
    pop_type     = 'hybrid' # Type of Population model being used
    pop_infected = 1000 # Number of initial infections
    beta         = 0.0079 # Beta value 
    asymp_factor = 2 # Multiply Beta by this factor for asymptotic infections
    contacts     = {'h':3.0, 's':20, 'w':20, 'c':20} # Mean for Poisson distributions of different contact layers
    
    pars = sc.objdict(
        use_waning   = True,
        pop_size     = pop_size,
        pop_infected = pop_infected,
        pop_scale    = pop_scale,
        pop_type     = pop_type,
        start_day    = start_day,
        end_day      = end_day,
        beta         = beta,
        asymp_factor = asymp_factor,
        contacts     = contacts,
        rand_seed    = 1,
        rescale      = True,
        verbose      = 0.01,
        rel_severe_prob = 0.7,
        rel_crit_prob = 15
    )
    
    
    if with_omicron == 1:
        sim = cv.Sim(pars=pars, datafile=data_path, end_day=end_day, location='uk')
    elif with_omicron == 0:
        sim = cv.Sim(pars=pars, end_day=end_day, location='uk')

    # Beta values for contact layers
    sbv = 0.63
    sbv_new = 0.8
    beta_dict  = sc.odict({'2020-02-14': [1.00, 1.00, 0.90, 0.90],
                           '2020-03-16': [1.00, 0.90, 0.80, 0.80],
                           #first lockdown starts
                           '2020-03-23': [1.00, 0.02, 0.20, 0.20],
                           #first lockdown ends
                           '2020-06-01': [1.00, 0.23, 0.40, 0.40],
                           '2020-06-15': [1.00, 0.38, 0.50, 0.50],
                           '2020-07-22': [1.15, 0.00, 0.30, 0.50],
                           '2020-07-29': [1.15, 0.00, 0.30, 0.70],
                           '2020-08-12': [1.15, 0.00, 0.30, 0.70],
                           '2020-07-19': [1.15, 0.00, 0.30, 0.70],
                           '2020-07-26': [1.15, 0.00, 0.30, 0.70],
                           #schools start in Sep 2020
                           '2020-09-02': [1.15, sbv, 0.50, 0.70],
                           '2020-10-01': [1.15, sbv, 0.50, 0.70],
                           '2020-10-16': [1.15, sbv, 0.50, 0.70],
                           #schools holiday Oct 2020
                           '2020-10-26': [1.15, 0.00, 0.50, 0.70],
                           #2nd lockdown starts
                           '2020-11-05': [1.15, sbv, 0.30, 0.30],
                           '2020-11-14': [1.15, sbv, 0.30, 0.40],
                           '2020-11-21': [1.15, sbv, 0.40, 0.50],
                           '2020-11-30': [1.15, sbv, 0.40, 0.50],
                           '2020-12-05': [1.15, sbv, 0.40, 0.50],
                           #2nd lockdown ends and opening for Christmas
                           '2020-12-10': [1.50, sbv, 0.40, 0.70],
                           '2020-12-17': [1.50, sbv, 0.40, 0.70],
                           '2020-12-24': [1.50, 0.00, 0.40, 0.70],
                           '2020-12-31': [1.50, 0.00, 0.40, 0.70],
                           #3rd lockdown starts
                           '2021-01-04': [1.00, 0.14, 0.20, 0.30],
                           '2021-01-11': [1.00, 0.14, 0.20, 0.30],
                           '2021-01-18': [1.00, 0.14, 0.20, 0.30],
                           '2021-01-30': [1.00, 0.14, 0.20, 0.30],
                           '2021-02-08': [1.00, 0.14, 0.20, 0.30],
                           '2021-02-15': [1.00, 0.00, 0.20, 0.30],
                           '2021-02-22': [1.00, 0.14, 0.20, 0.30],
                           #3rd lockdown ends and reopening starts in 4 steps
                           #schools open in March 2021 - step 1 
                           '2021-03-08': [1.05, sbv, 0.20, 0.25],
                           '2021-03-15': [1.05, sbv, 0.20, 0.25],
                           '2021-03-22': [1.05, sbv, 0.20, 0.25],
                           #Easter school holiday
                           '2021-03-29': [1.05, 0.00, 0.25, 0.25],
                           #further relaxation measures - step 2
                           '2021-04-12': [1.05, 0.00, 0.30, 0.25],
                           '2021-04-19': [1.05, sbv, 0.30, 0.30],
                           '2021-04-26': [1.05, sbv, 0.30, 0.30],
                           '2021-05-03': [1.05, sbv, 0.30, 0.30],
                           '2021-05-10': [1.05, sbv, 0.30, 0.30],
                           #some further relaxation  - step 3
                           '2021-05-17': [1.05, sbv, 0.30, 0.50],
                           '2021-05-21': [1.05, sbv, 0.30, 0.50],
                           #May half-term
                           '2021-05-31': [1.05, 0.00, 0.30, 0.50],
                           #after May half-term
                           '2021-06-07': [1.05, sbv, 0.30, 0.50],
                           '2021-06-14': [1.05, sbv, 0.30, 0.50],
                           #to fit data we need to increase community mixing from 19/06/2021  
                           '2021-06-19': [1.05, sbv, 0.40, 0.70],
                           '2021-06-21': [1.05, sbv, 0.40, 0.70],
                           #to fit data we need to increase community mixing further from 28/06/2021                          
                           '2021-06-28': [1.3, sbv, 0.40, 1.40],
                           '2021-07-05': [1.3, sbv, 0.40, 1.40],
                           '2021-07-12': [1.3, sbv, 0.40, 1.40],
                           #cases start to drop from middle of July and community mixing falls
                           '2021-07-19': [1.05, 0.00, 0.40, 0.60],
                           #easing of socal distancing measures - delayed step 4
                           #schools stay shut and a lot of people are away from work/community as its summer holiday
                           '2021-07-26': [1.05, 0.00, 0.40, 0.60],
                           '2021-08-02': [1.05, 0.00, 0.40, 0.60],
                           '2021-08-09': [1.05, 0.00, 0.40, 0.60],
                           '2021-08-16': [1.05, 0.00, 0.40, 0.60],
                           '2021-08-23': [1.05, 0.00, 0.40, 0.60],
                           #reopening schools in Sep 2021, less social distancing in schools, less community and work contact to keep schools open
                           '2021-09-07': [1.05, sbv, 0.30, 0.50],
                           '2021-09-15': [1.05, sbv, 0.30, 0.50],
                           '2021-09-29': [1.05, sbv, 0.30, 0.50],
                           '2021-10-15': [1.05, sbv, 0.30, 0.50],
                           #october half term
                           '2021-10-22': [1.05, 0.00, 0.30, 0.50],
                           '2021-10-29': [1.05, 0.00, 0.30, 0.50],
                           '2021-11-05': [1.05, sbv, 0.30, 0.50],
                           '2021-11-12': [1.05, sbv, 0.30, 0.50],
                           '2021-11-19': [1.05, sbv, 0.30, 0.50],
                           '2021-11-26': [1.05, sbv, 0.30, 0.50],
                           #mixing increases towards chrismas, especially within households and the community
                           '2021-12-01': [1.20, sbv, 0.30, 0.60],
                           '2021-12-09': [1.40, sbv, 0.40, 0.70],
                           '2021-12-16': [1.60, sbv, 0.40, 0.70],
                           #schools holidays
                           '2021-12-20': [2, 0.00, 0.40, 1.5],
                           '2021-12-31': [2, 0.00, 0.40, 1.5],
                           '2022-01-01': [2, 0.00, 0.40, 1.5],
                           #PlanB and schools open
                           
                           '2022-01-04': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-11': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-18': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-30': [1.0, sbv_new, 0.50, 0.60],
                           '2022-02-08': [1.0, sbv_new, 0.50, 0.60],
                           #february half term
                           '2022-02-15': [1.0, 0.00, 0.50, 0.70],
                           #school reopens
                           '2022-02-22': [1.0, 0.9, 0.50, 0.70],
                           #easter holidays
                           '2022-04-09': [1.0, 0.00, 0.50, 0.70],
                           #school reopens
                           '2022-04-22': [1.0, 0.9, 0.5, 0.7],
                           #may half term
                           '2022-05-28': [1.0, 0.00, 0.50, 0.70],
                           #school reopens
                           '2022-06-03': [1.0, 0.9, 0.50, 0.90],
                           #summer holidays
                           '2022-07-23': [1.0, 0.00, 0.4, 0.5],
                           #school reopens
                           '2022-08-31': [1.0, 0.9, 0.5, 0.5],
                           #october half term
                           '2022-10-22': [1.0, 0.00, 0.5, 0.5],
                           #school reopens
                           '2022-10-29': [1.0, 0.9, 0.5, 0.6],
                           #christmas holidays
                           '2022-12-19': [2.4, 0.00, 0.5, 1.3],
                           '2023-01-04': [1, 0.9, 0.5, 0.7], 
                           })
                          
    beta_days = list(beta_dict.keys())
    h_beta = cv.change_beta(days=beta_days, changes=[c[0] for c in beta_dict.values()], layers='h')
    s_beta = cv.change_beta(days=beta_days, changes=[c[1] for c in beta_dict.values()], layers='s')
    w_beta = cv.change_beta(days=beta_days, changes=[c[2] for c in beta_dict.values()], layers='w')
    c_beta = cv.change_beta(days=beta_days, changes=[c[3] for c in beta_dict.values()], layers='c')
    interventions = [h_beta, w_beta, s_beta, c_beta]

    # adding different variants
    # Add B.1.177 strain to be present by September 2020
    variants = []
    b1177 = cv.variant(label='B.1.177', variant=cvp.get_variant_pars()['beta'], days=np.arange(sim.day('2020-08-10'), sim.day('2020-08-20')), n_imports=3000)
    b1177.p['rel_beta']        = 1.2
    b1177.p['rel_severe_prob'] = 0.2
    b1177.p['rel_crit_prob']  = 23
    variants += [b1177]
    
    # Add Alpha strain to be present by October 2020
    b117 = cv.variant(label = 'Alpha', variant=cvp.get_variant_pars()['alpha'], days=np.arange(sim.day('2020-10-20'), sim.day('2020-10-30')), n_imports=3000)
    b117.p['rel_beta']        = 1.8
    b117.p['rel_severe_prob'] = 1.01
    b117.p['rel_crit_prob']  = 100
    b117.p['rel_death_prob']  = 0.7
    variants += [b117]
    
    # Add Delta strain to be present by April 2021
    b16172 = cv.variant(label = 'Delta', variant=cvp.get_variant_pars()['delta'], days=np.arange(sim.day('2021-04-15'), sim.day('2021-04-20')), n_imports=4000)
    b16172.p['rel_beta']         = 2.6
    b16172.p['rel_severe_prob']  = 0.28
    b16172.p['rel_crit_prob']  = 25
    b16172.p['rel_death_prob']  = 0.4
    variants += [b16172]
    
    if with_omicron == 1:
        number_imports = 4000
    elif with_omicron == 0:
        number_imports = 0
    
    # Add Omicron BA.1 strain to be present by November 2021
    ba1 = cv.variant(label='Omicron BA.1', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-10-16'), sim.day('2021-10-23')), n_imports=number_imports)
    ba1.p['rel_beta']         = 3.6
    ba1.p['rel_severe_prob']  = 0.3
    ba1.p['rel_crit_prob']  = 0.15
    ba1.p['rel_death_prob']  = 0.9
    variants += [ba1]
    
    # Add Omicron BA.1.1 strain to be present by November 2021
    ba11 = cv.variant(label='Omicron BA.1.1', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-10-23'), sim.day('2021-10-30')), n_imports=number_imports)  
    ba11.p['rel_beta']         = 3.1
    ba11.p['rel_severe_prob']  = 0.3
    ba11.p['rel_crit_prob']  = 0.15
    ba11.p['rel_death_prob'] = 0.5
    variants += [ba11]
    
    # Add Omicron BA.2 strain to be present by December 2021
    ba2 = cv.variant(label='Omicron BA.2', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-12-18'), sim.day('2021-12-25')), n_imports=number_imports)   
    ba2.p['rel_beta']         = 5.1
    ba2.p['rel_severe_prob']  = 0.2
    ba2.p['rel_crit_prob']  = 0.07
    ba2.p['rel_death_prob']  = 0.5
    variants += [ba2]
    
    # Add Omicron BA.4 strain to be present by April 2022
    ba4 = cv.variant(label='Omicron BA.4', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2022-03-19'), sim.day('2022-03-26')), n_imports=number_imports)    
    ba4.p['rel_beta']         = 5
    ba4.p['rel_severe_prob']  = 0.35
    ba4.p['rel_crit_prob']  = 0.05
    ba4.p['rel_death_prob']  = 1.55
    variants += [ba4]
    
    # Add Omicron BA.5 strain to be present by April 2022
    ba5 = cv.variant(label='Omicron BA.5', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2022-03-26'), sim.day('2022-04-02')), n_imports=number_imports)
    ba5.p['rel_beta']         = 5.5
    ba5.p['rel_severe_prob']  = 0.35
    ba5.p['rel_crit_prob']  = 0.05
    ba5.p['rel_death_prob']  = 1.55
    variants += [ba5]
    
    # Add Omicron XBB strain to be present by October 2022
    xbb = cv.variant(label='Omicron XBB', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2022-10-01'), sim.day('2022-10-15')), n_imports=number_imports)
    xbb.p['rel_beta']         = 5.2
    xbb.p['rel_severe_prob']  = 0.35
    xbb.p['rel_crit_prob']  = 0.05
    xbb.p['rel_death_prob']  = 1.55
    variants += [xbb]
    
    sim['variants'] = variants
    sim.init_variants()
    sim.init_immunity()
    sim['immunity']
    
    #add variant cross immunities
    prior_alpha = {'wild': 0.5, 'Alpha': 1, 
                   'Delta': 0.689, 'B.1.177': 0.5, 'Omicron BA.1': 0.050, 
                   'Omicron BA.1.1': 0.050, 'Omicron BA.2': 0.050, 
                   'Omicron BA.4': 0.050, 'Omicron BA.5': 0.050, 'Omicron XBB': 0.050}
    
    prior_delta = {'wild': 0.374, 'Alpha': 0.689, 
                   'Delta': 1, 'B.1.177': 0.086, 'Omicron BA.1': 0.040, 
                   'Omicron BA.1.1': 0.040, 'Omicron BA.2': 0.040, 
                   'Omicron BA.4': 0.040, 'Omicron BA.5': 0.040, 'Omicron XBB': 0.040}
    
    prior_b1177 = {'wild': 0.066, 'Alpha': 0.500, 
                   'Delta': 0.086, 'B.1.177': 1.000, 'Omicron BA.1': 0.050, 
                   'Omicron BA.1.1': 0.050, 'Omicron BA.2': 0.050, 
                   'Omicron BA.4': 0.050, 'Omicron BA.5': 0.050, 'Omicron XBB': 0.050}
    
    prior_ba1 = {'wild': 0.050, 'Alpha': 0.050, 
                 'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 1.000,
                 'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.600, 
                 'Omicron BA.4': 0.300, 'Omicron BA.5': 0.300, 'Omicron XBB': 0.300}
    
    prior_ba11 = {'wild': 0.050, 'Alpha': 0.050, 
                  'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.200, 
                  'Omicron BA.1.1': 1.000, 'Omicron BA.2': 0.600, 
                  'Omicron BA.4': 0.200, 'Omicron BA.5': 0.200, 'Omicron XBB': 0.100}
    
    prior_ba2 = {'wild': 0.050, 'Alpha': 0.050, 
                 'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.600, 
                 'Omicron BA.1.1': 0.600, 'Omicron BA.2': 1.000, 
                 'Omicron BA.4': 0.8, 'Omicron BA.5': 0.6, 'Omicron XBB': 0.6}
    
    prior_ba4 = {'wild': 0.050, 'Alpha': 0.050, 
                 'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.100, 
                 'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.8, 
                 'Omicron BA.4': 1.000, 'Omicron BA.5': 0.500, 'Omicron XBB': 0.400}
    
    prior_ba5 = {'wild': 0.050, 'Alpha': 0.050,  
                 'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.300, 
                 'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.6, 
                 'Omicron BA.4': 0.500, 'Omicron BA.5': 1.000, 'Omicron XBB': 0.400}
    
    prior_xbb = {'wild': 0.050, 'Alpha': 0.050, 
                 'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.300, 
                 'Omicron BA.1.1': 0.100, 'Omicron BA.2': 0.6, 
                 'Omicron BA.4': 0.400, 'Omicron BA.5': 0.400, 'Omicron XBB': 1.000}
    
    pre_alpha = {'wild': 0.5, 'Alpha': 1, 
                   'Delta': 0.689, 'B.1.177': 0.5, 'Omicron BA.1': 0.050, 
                   'Omicron BA.1.1': 0.050, 'Omicron BA.2': 0.050, 
                   'Omicron BA.4': 0.050, 'Omicron BA.5': 0.050, 'Omicron XBB': 0.050}
    
    pre_delta = {'wild': 0.374, 'Alpha': 0.689, 
                   'Delta': 1, 'B.1.177': 0.086, 'Omicron BA.1': 0.040, 
                   'Omicron BA.1.1': 0.040, 'Omicron BA.2': 0.040, 
                   'Omicron BA.4': 0.040, 'Omicron BA.5': 0.040, 'Omicron XBB': 0.040}
    
    pre_b1177 = {'wild': 0.066, 'Alpha': 0.500,  
                 'Delta': 0.086, 'B.1.177': 1.000, 'Omicron BA.1': 0.050, 
                 'Omicron BA.1.1': 0.050, 'Omicron BA.2': 0.050, 
                 'Omicron BA.4': 0.050, 'Omicron BA.5': 0.050, 'Omicron XBB': 0.050}
    
    pre_ba1 = {'wild': 0.050, 'Alpha': 0.050, 
               'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 1.000,
               'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.600, 
               'Omicron BA.4': 0.300, 'Omicron BA.5': 0.300, 'Omicron XBB': 0.300}
    
    pre_ba11 = {'wild': 0.050, 'Alpha': 0.050, 
                'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.200, 
                'Omicron BA.1.1': 1.000, 'Omicron BA.2': 0.600, 
                'Omicron BA.4': 0.200, 'Omicron BA.5': 0.200, 'Omicron XBB': 0.100}
    
    pre_ba2 = {'wild': 0.050, 'Alpha': 0.050,  
               'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.600, 
               'Omicron BA.1.1': 0.600, 'Omicron BA.2': 1.000, 
               'Omicron BA.4': 0.8, 'Omicron BA.5': 0.6, 'Omicron XBB': 0.6}
    
    pre_ba4 = {'wild': 0.050, 'Alpha': 0.050, 
               'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.100, 
               'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.8, 
               'Omicron BA.4': 1.000, 'Omicron BA.5': 0.500, 'Omicron XBB': 0.400}
    
    pre_ba5 = {'wild': 0.050, 'Alpha': 0.050,  
               'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.300, 
               'Omicron BA.1.1': 0.200, 'Omicron BA.2': 0.6, 
               'Omicron BA.4': 0.500, 'Omicron BA.5': 1.000, 'Omicron XBB': 0.400}
    
    pre_xbb = {'wild': 0.050, 'Alpha': 0.050, 
               'Delta': 0.040, 'B.1.177': 0.050, 'Omicron BA.1': 0.300, 
               'Omicron BA.1.1': 0.100, 'Omicron BA.2': 0.6, 
               'Omicron BA.4': 0.400, 'Omicron BA.5': 0.400, 'Omicron XBB': 1.000}
    
    for k,v in sim['variant_map'].items():
        if v == 'Alpha':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_alpha[j_lab]
                sim['immunity'][j][k] = pre_alpha[j_lab]
        if v == 'Delta':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_delta[j_lab]
                sim['immunity'][j][k] = pre_delta[j_lab]
        if v == 'B.1.177':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_b1177[j_lab]
                sim['immunity'][j][k] = pre_b1177[j_lab]
        if v == 'Omicron BA.1':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba1[j_lab]
                sim['immunity'][j][k] = pre_ba1[j_lab]
        if v == 'Omicron BA.1.1':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba11[j_lab]
                sim['immunity'][j][k] = pre_ba11[j_lab]
        if v == 'Omicron BA.2':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba2[j_lab]
                sim['immunity'][j][k] = pre_ba2[j_lab]
        if v == 'Omicron BA.4':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba4[j_lab]
                sim['immunity'][j][k] = pre_ba4[j_lab]
        if v == 'Omicron BA.5':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba5[j_lab]
                sim['immunity'][j][k] = pre_ba5[j_lab]
        if v == 'Omicron XBB':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_xbb[j_lab]
                sim['immunity'][j][k] = pre_xbb[j_lab]
        
    #define vaccine age groups, start day of vaccination and days to reach        
      
    # vaccination parameters for the different adoelescent vaccine scenarios
    
    days_16 = [50,60,70,80,90,100,110,120,130,140,100]
    days_12 = [71,81,91,101,111,121,131,141,151,161,121]
    probs_16 = [0,0.0022,0.0032,0.0044,0.0058,0.0070,0.0081,0.012,0.0125,0.016,0.0086]
    probs_12 = [0,0.0014,0.0025,0.0033,0.0046,0.0056,0.0070,0.008,0.0105,0.012,0.0051]
    start_day_16 = ['2021-08-01','2021-08-15','2021-08-29','2021-09-12','2021-09-26','2021-10-10','2021-08-23']
    start_day_12 = ['2021-08-29','2021-09-12','2021-09-26','2021-10-10','2021-10-24','2021-11-07','2021-09-20']
    
    
    vx_rollout = {
        90: dict(start_age=90, end_age=100, start_day='2020-12-08', days_to_reach=41),
        85: dict(start_age=85, end_age=90, start_day='2020-12-08', days_to_reach=41),
        80: dict(start_age=80, end_age=85, start_day='2020-12-08', days_to_reach=41),
        75: dict(start_age=75, end_age=80, start_day='2021-01-18', days_to_reach=19),
        70: dict(start_age=70, end_age=75, start_day='2021-01-29', days_to_reach=18),
        65: dict(start_age=65, end_age=70, start_day='2021-02-15', days_to_reach=15),
        60: dict(start_age=60, end_age=65, start_day='2021-03-01', days_to_reach=16),
        55: dict(start_age=55, end_age=60, start_day='2021-03-06', days_to_reach=15),
        50: dict(start_age=50, end_age=55, start_day='2021-03-17', days_to_reach=27),
        45: dict(start_age=45, end_age=50, start_day='2021-04-13', days_to_reach=17),
        40: dict(start_age=40, end_age=45, start_day='2021-04-26', days_to_reach=19),
        35: dict(start_age=35, end_age=40, start_day='2021-05-13', days_to_reach=15),
        30: dict(start_age=30, end_age=35, start_day='2021-05-20', days_to_reach=19),
        25: dict(start_age=25, end_age=30, start_day='2021-06-08', days_to_reach=15),
        18: dict(start_age=18, end_age=25, start_day='2021-06-15', days_to_reach=50),
        16: dict(start_age=16, end_age=18, start_day=start_day_16[day_start], days_to_reach=days_16[per_vac]),
        12: dict(start_age=12, end_age=16, start_day=start_day_12[day_start], days_to_reach=days_12[per_vac]),
        5: dict(start_age=5, end_age=12, start_day='2022-03-01', days_to_reach=31),
    }
    
    def set_subtargets(vx_phase):
      return lambda sim: cv.true((sim.people.age >= vx_phase['start_age']) * (sim.people.age < vx_phase['end_age']))
    
    #daily probability each age group gets vaccinated, calibrated with the days to reach vaccinated to give the right final uptake when compared to data
    
    subtarget_dict = {}
    for age, vx_phase in vx_rollout.items():
        if (age>=80):
            vx_phase['daily_prob'] =0.075
        elif (age>=70)*(age<80):
            vx_phase['daily_prob'] =0.15
        elif (age>=65)*(age<70):
            vx_phase['daily_prob'] =0.162
        elif (age>=60)*(age<65):
            vx_phase['daily_prob'] =0.136
        elif (age>=55)*(age<60):
            vx_phase['daily_prob'] =0.135
        elif (age>=50)*(age<55):
            vx_phase['daily_prob'] =0.071
        elif (age>=45)*(age<50):
            vx_phase['daily_prob'] =0.093
        elif (age>=40)*(age<45):
            vx_phase['daily_prob'] =0.074
        elif (age>=35)*(age<40):
            vx_phase['daily_prob'] =0.081
        elif (age>=30)*(age<35):
            vx_phase['daily_prob'] =0.0578
        elif (age>=25)*(age<30):
            vx_phase['daily_prob'] =0.0705
        elif (age>=18)*(age<25):
            vx_phase['daily_prob'] =0.024 
        elif (age>=16)*(age<18):
            vx_phase['daily_prob'] =probs_16[per_vac]
        elif (age>=12)*(age<16):
            vx_phase['daily_prob'] =probs_12[per_vac]
        elif (age>=5)*(age<12):
            vx_phase['daily_prob'] =0.0034
        subtarget_dict[age] = {'inds': set_subtargets(vx_phase),
                               'vals': vx_phase['daily_prob']}
    

    # Test and Trace interventions
    tc_day = sim.day('2020-03-16') #intervention of some testing (tc) starts on 16th March and we run until 1st April when it increases
    te_day = sim.day('2020-04-01') #intervention of some testing (te) starts on 1st April and we run until 1st May when it increases
    tt_day = sim.day('2020-05-01') #intervention of increased testing (tt) starts on 1st May
    tti_day= sim.day('2020-06-01') #intervention of tracing and enhanced testing (tti) starts on 1st June
    tti_day_july= sim.day('2020-07-01') #intervention of tracing and enhanced testing (tti) at different levels starts on 1st July
    tti_day_august= sim.day('2020-08-01') #intervention of tracing and enhanced testing (tti) at different levels starts on 1st August
    tti_day_sep= sim.day('2020-09-01')
    tti_day_oct= sim.day('2020-10-01')
    tti_day_nov= sim.day('2020-11-01')
    tti_day_dec= sim.day('2020-12-01')
    tti_day_jan= sim.day('2021-01-01')
    tti_day_feb= sim.day('2021-02-01')
    tti_day_march= sim.day('2021-03-08')
    tti_day_june21= sim.day('2021-06-20')
    tti_day_july1_21= sim.day('2021-07-10')
    tti_day_july2_21= sim.day('2021-07-19')#19
    tti_day_august21= sim.day('2021-08-02')
    tti_day_sep21= sim.day('2021-09-20')#01
    tti_day_oct21= sim.day('2021-10-22')
    tti_day_nov21= sim.day('2021-11-07')
    tti_day_dec21= sim.day('2021-12-01')
    tti_day_dec2_21= sim.day('2021-12-10')
    tti_day_jan22= sim.day('2022-01-05')
    tti_day_feb1_22= sim.day('2022-02-01')
    tti_day_feb2_22= sim.day('2022-02-24')
    tti_day_march22= sim.day('2022-03-20')
    tti_day_april1_22= sim.day('2022-04-01')
    tti_day_april2_22= sim.day('2022-04-20')
    tti_day_june22= sim.day('2022-06-01')
    tti_day_july22= sim.day('2022-07-01')

    # Symptomatic testing probabilities
    s_prob_april = 0.012
    s_prob_may   = 0.012
    s_prob_june = 0.04769
    s_prob_july = 0.04769
    s_prob_august = 0.04769
    s_prob_sep = 0.07769
    s_prob_oct = 0.07769
    s_prob_nov = 0.07769
    s_prob_dec = 0.07769
    s_prob_jan = 0.07769
    s_prob_feb = 0.06769
    s_prob_march = 0.08769
    #to match the increase in June-mid July from optuna increased testing is necessary
    s_prob_june21 = 0.19769
    s_prob_july1_21 = 0.19769
    #to match the decrease from mid July from optuna decreased testing is necessary
    s_prob_july2_21 = 0.04769
    s_prob_august21 = 0.04769
    s_prob_sep21 =0.06769
    s_prob_oct21 =0.06769
    s_prob_nov21 = 0.07769
    s_prob_dec21 = 0.12
    s_prob_dec2_21 = 0.15
    s_prob_jan22 = 0.10
    s_prob_feb1_22 = 0.03
    s_prob_feb2_22 = 0.03
    s_prob_march22 = 0.02
    s_prob_april1_22 = 0.008
    s_prob_april2_22 = 0.008
    s_prob_june22 = 0.008
    s_prob_july22 = 0.008

    t_delay       = 1.0

    # Isolation factor
    #isolation may-june 2020
    iso_vals = [{k:0.2 for k in 'hswc'}]
    #isolation july 2020
    iso_vals1 = [{k:0.4 for k in 'hswc'}]
    #isolation september 2020
    iso_vals2 = [{k:0.6 for k in 'hswc'}]
    #isolation october 2020
    iso_vals3 = [{k:0.6 for k in 'hswc'}]
    #isolation november 2020
    iso_vals4 = [{k:0.2 for k in 'hswc'}]
     #isolation december 2020
    iso_vals5 = [{k:0.5 for k in 'hswc'}]
    #isolation March 2021
    iso_vals6 = [{k:0.5 for k in 'hswc'}]
    #isolation from 20 June 2021 reduced
    iso_vals7 = [{k:0.8 for k in 'hswc'}] 
    #isolation from 02 August 2021
    iso_vals9 = [{k:0.2 for k in 'hswc'}]
    #isolation from Sep 2021
    iso_vals10 = [{k:0.6 for k in 'hswc'}]
    #isolation from Dec 2021
    iso_vals11 = [{k:0.7 for k in 'hswc'}]
    #isolation from 24 February 2021
    iso_vals12 = [{k:0.8 for k in 'hswc'}]
    #isolation from April 2021
    iso_vals13 = [{k:0.8 for k in 'hswc'}]

    # Testing and isolation intervention
    interventions += [
        cv.test_prob(symp_prob=0.009, asymp_prob=0.0, symp_quar_prob=0.0, start_day=tc_day, end_day=te_day-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_april, asymp_prob=0.0, symp_quar_prob=0.0, start_day=te_day, end_day=tt_day-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_may, asymp_prob=0.00076, symp_quar_prob=0.0, start_day=tt_day, end_day=tti_day-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_june, asymp_prob=0.00076, symp_quar_prob=0.0, start_day=tti_day, end_day=tti_day_july-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_july, asymp_prob=0.00076, symp_quar_prob=0.0, start_day=tti_day_july, end_day=tti_day_august-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_august, asymp_prob=0.0028, symp_quar_prob=0.0, start_day=tti_day_august, end_day=tti_day_sep-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_sep, asymp_prob=0.0028, symp_quar_prob=0.0, start_day=tti_day_sep, end_day=tti_day_oct-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_oct, asymp_prob=0.0028, symp_quar_prob=0.0, start_day=tti_day_oct, end_day=tti_day_nov-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_nov, asymp_prob=0.0040, symp_quar_prob=0.0, start_day=tti_day_nov, end_day=tti_day_dec-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_dec, asymp_prob=0.0063, symp_quar_prob=0.0, start_day=tti_day_dec, end_day=tti_day_jan-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_jan, asymp_prob=0.0063, symp_quar_prob=0.0, start_day=tti_day_jan, end_day=tti_day_feb-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_feb, asymp_prob=0.0063, symp_quar_prob=0.0, start_day=tti_day_feb, end_day=tti_day_march-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_march, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_march, end_day=tti_day_june21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_june21, asymp_prob=0.02, symp_quar_prob=0.0, start_day=tti_day_june21, end_day=tti_day_july1_21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_july1_21, asymp_prob=0.016, symp_quar_prob=0.0, start_day=tti_day_july1_21, end_day=tti_day_july2_21-1, test_delay=t_delay), 
        cv.test_prob(symp_prob=s_prob_july2_21, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_july2_21, end_day=tti_day_august21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_august21, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_august21, end_day=tti_day_sep21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_sep21, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_sep21, end_day=tti_day_oct21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_oct21, asymp_prob=0.004, symp_quar_prob=0.0, start_day=tti_day_oct21, end_day=tti_day_nov21-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_nov21, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_nov21, end_day=tti_day_dec21-1, test_delay=t_delay),# 0.008
        cv.test_prob(symp_prob=s_prob_dec21, asymp_prob=0.016, symp_quar_prob=0.0, start_day=tti_day_dec21, end_day=tti_day_dec2_21-1,test_delay=t_delay),# 0.008
        cv.test_prob(symp_prob=s_prob_dec2_21, asymp_prob=0.02, symp_quar_prob=0.0, start_day=tti_day_dec2_21, end_day=tti_day_jan22-1,test_delay=t_delay),#0.024
        cv.test_prob(symp_prob=s_prob_jan22, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_jan22, end_day=tti_day_feb1_22-1, test_delay=t_delay),# 0.005
        cv.test_prob(symp_prob=s_prob_feb1_22, asymp_prob=0.008, symp_quar_prob=0.0, start_day=tti_day_feb1_22, end_day=tti_day_feb2_22-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_feb2_22, asymp_prob=0.004, symp_quar_prob=0.0, start_day=tti_day_feb2_22, end_day=tti_day_march22-1, test_delay=t_delay),#0.04
        cv.test_prob(symp_prob=s_prob_march22, asymp_prob=0.004, symp_quar_prob=0.0, start_day=tti_day_march22, end_day = tti_day_april1_22-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_april1_22, asymp_prob=0.0008, symp_quar_prob=0.0, start_day=tti_day_april1_22, end_day = tti_day_april2_22-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_april2_22, asymp_prob=0.0008, symp_quar_prob=0.0, start_day=tti_day_april2_22, end_day = tti_day_june22-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_june22, asymp_prob=0.0008, symp_quar_prob=0.0, start_day=tti_day_june22, end_day = tti_day_july22-1, test_delay=t_delay),
        cv.test_prob(symp_prob=s_prob_july22, asymp_prob=0.0008, symp_quar_prob=0.0, start_day=tti_day_july22, test_delay=t_delay),
        cv.contact_tracing(trace_probs={'h': 1, 's': 0.8, 'w': 0.8, 'c': 0.1},
                           trace_time={'h': 0, 's': 1, 'w': 1, 'c': 2},
                           start_day='2020-06-01', end_day='2021-07-12',
                           quar_period=10),
        cv.contact_tracing(trace_probs={'h': 1, 's': 0.8, 'w': 0.8, 'c': 0.3},
                           trace_time={'h': 0, 's': 1, 'w': 1, 'c': 2},
                           start_day='2021-07-12', end_day='2021-09-10',
                           quar_period=10),
        cv.contact_tracing(trace_probs={'h': 1, 's': 0.8, 'w': 0.8, 'c': 0.1},
                           trace_time={'h': 0, 's': 1, 'w': 1, 'c': 2},
                           start_day='2021-09-10', end_day='2022-02-24',
                           quar_period=7),
        cv.contact_tracing(trace_probs={'h': 1, 's': 0.8, 'w': 0.8, 'c': 0.1},
                           trace_time={'h': 0, 's': 1, 'w': 1, 'c': 2},
                           start_day='2022-02-24', end_day='2022-04-01',
                           quar_period=7),
        cv.contact_tracing(trace_probs={'h': 1, 's': 0.8, 'w': 0.8, 'c': 0.1},
                           trace_time={'h': 0, 's': 1, 'w': 1, 'c': 2},
                           start_day='2022-04-01', end_day='2023-04-30',
                           quar_period=5),
        cv.dynamic_pars({'iso_factor': {'days': te_day, 'vals': iso_vals}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_july, 'vals': iso_vals1}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_sep, 'vals': iso_vals2}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_oct, 'vals': iso_vals3}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_nov, 'vals': iso_vals4}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_dec, 'vals': iso_vals5}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_march, 'vals': iso_vals6}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_june21, 'vals': iso_vals7}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_august21, 'vals': iso_vals9}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_sep21, 'vals': iso_vals10}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_dec21, 'vals': iso_vals11}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_feb2_22, 'vals': iso_vals12}}),
        cv.dynamic_pars({'iso_factor': {'days': tti_day_april1_22, 'vals': iso_vals13}})]
    
    # Omicron goes through infectious stages quicker
    
    def change_infect(sim):
        if sim.t == tti_day_nov21:
            sim['dur']['exp2inf']['par1'] = 3.4        
    
    
    def change_hosp(sim):
        if sim.t == tti_day_nov21:
            sim['dur']['sev2rec']['par1'] = 5.5

    
    interventions += [change_hosp, change_infect]

    # Define the vaccines
    dose_pars = cvp.get_vaccine_dose_pars()['az']
    dose_pars['interval'] = 7 * 8
    variant_pars = {'wild': 1.0, 'Alpha': 1/2.3, 
                    'Delta': 1/6.2, 'B.1.177': 1/9, 'Omicron BA.1': 1/2.9, 
                    'Omicron BA.1.1': 1/2.9, 'Omicron BA.2': 1/2.9, 
                    'Omicron BA.4': 1/2.9, 'Omicron BA.5': 1/2.9, 'Omicron XBB': 1/2.9}
    az_vaccine = sc.mergedicts({'label':'az_uk'}, sc.mergedicts(dose_pars, variant_pars)) 
    
    dose_pars = cvp.get_vaccine_dose_pars()['pfizer']
    dose_pars['interval'] = 7 * 8
    variant_pars = cvp.get_vaccine_variant_pars()['pfizer']
    variant_pars = {'wild': 1.0, 'Alpha': 1/2.0, 
                    'Delta': 1/2.9, 'B.1.177': 1/10.3, 'Omicron BA.1': 1/4.5, 
                    'Omicron BA.1.1': 1/4.5, 'Omicron BA.2': 1/4.5, 
                    'Omicron BA.4': 1/4.5, 'Omicron BA.5': 1/4.5, 'Omicron XBB': 1/4.5}
    pfizer_vaccine = sc.mergedicts({'label':'pfizer_uk'}, sc.mergedicts(dose_pars, variant_pars))
    
    # Slower dose roll out of Pfizer for those aged over 80 and aged below 18
    dose_pars = cvp.get_vaccine_dose_pars()['pfizer']
    dose_pars['interval'] = 7 * 12
    variant_pars = cvp.get_vaccine_variant_pars()['pfizer']
    variant_pars = {'wild': 1.0, 'Alpha': 1/2.0, 
                    'Delta': 1/2.9, 'B.1.177': 1/10.3, 'Omicron BA.1': 1/4.5, 
                    'Omicron BA.1.1': 1/4.5, 'Omicron BA.2': 1/4.5, 
                    'Omicron BA.4': 1/4.5, 'Omicron BA.5': 1/4.5, 'Omicron XBB': 1/4.5}
    pfizer_vaccine_slow = sc.mergedicts({'label':'pfizer_uk_slow'}, sc.mergedicts(dose_pars, variant_pars))

    # Loop over vaccination in different ages
    for age,vx_phase in vx_rollout.items():
        if(age >= 40 and age < 65):
            vaccine = az_vaccine
        elif ((age >=5 and age <18)or (age>=80)):
            vaccine = pfizer_vaccine_slow
        else:
            vaccine = pfizer_vaccine
        vx_start_day = sim.day(vx_phase['start_day'])
        vx_end_day = vx_start_day + vx_phase['days_to_reach']
        days = np.arange(vx_start_day, vx_end_day)

        vx = cv.vaccinate_prob(vaccine=vaccine, days=days, subtarget=subtarget_dict[age], label=f'Vaccinate {age}')
        interventions += [vx]
        
    # Define booster as a custom vaccination but with parameters like pfizer and moderna as these are used in England as boosters
    dict1 = dict(
        nab_eff=sc.dcp(sim['nab_eff']),
        nab_init=None,
        nab_boost=3,
        doses=1,
        interval=None,
        wild=1.0,
        alpha=1/2.1,
        delta=1/4.5,)
    
    variantdict = {'Alpha':1/2.1, 'Delta':1/4.5, 'Omicron BA.1':1/4.8,
        'B.1.177':1/9.6,
        'Omicron BA.1.1':1/4.8,
        'Omicron BA.2':1/4.8,
        'Omicron BA.4':1/4.8, 
        'Omicron BA.5':1/4.8,
        'Omicron XBB':1/4.8}
    
    booster = sc.mergedicts(dict1, variantdict)
    booster2 = sc.mergedicts(dict1, variantdict)
    booster3 = sc.mergedicts(dict1, variantdict)
    booster4= sc.mergedicts(dict1, variantdict)

    booster_target = {'inds': lambda sim: cv.true(sim.people.doses != 2|(sim.people.age<18)),
                      'vals': 0}  # Only give boosters to people who have had 2 doses
    booster_target2 = {'inds': lambda sim: cv.true((sim.people.doses != 3)|(sim.people.age < 75)),
                      'vals': 0} # Only give Spring second booster to those aged over 75 who have already been boosted once
    booster_target3 = {'inds': lambda sim: cv.true((sim.people.doses != 3)|(sim.people.age < 50)|(sim.people.age>=75)),
                      'vals': 0} # Give Spring second booster to those aged over 50 who have already been boosted once
    booster_target4 = {'inds': lambda sim: cv.true((sim.people.doses != 2)|(sim.people.age <12)|(sim.people.age>=18)),
                      'vals': 0} # Give booster to adolescents as well

    def num_boosters(sim):
        if sim.t < sim.day('2021-07-22'):                      return 0
        if (sim.t>=sim.day('2021-07-22'))*(sim.t < sim.day('2021-08-22')):      return 425
        if (sim.t>=sim.day('2021-08-22'))*(sim.t < sim.day('2021-09-22')):      return 4231
        if (sim.t>=sim.day('2021-09-22'))*(sim.t < sim.day('2021-10-22')):      return 156551
        if (sim.t>=sim.day('2021-10-22'))*(sim.t < sim.day('2021-11-22')):      return 257568
        if (sim.t>=sim.day('2021-11-22'))*(sim.t < sim.day('2021-12-22')):      return 450490
        if (sim.t>=sim.day('2021-12-22'))*(sim.t < sim.day('2022-01-22')):      return 131027
        if (sim.t>=sim.day('2022-01-22'))*(sim.t < sim.day('2022-02-22')):      return 27382
        if (sim.t>=sim.day('2022-02-22'))*(sim.t < sim.day('2022-03-22')):      return 15550
        if (sim.t>=sim.day('2022-03-22'))*(sim.t < sim.day('2022-04-22')):      return 12033
        if (sim.t>=sim.day('2022-04-22'))*(sim.t < sim.day('2022-05-22')):      return 10959
        if (sim.t>=sim.day('2022-05-22'))*(sim.t < sim.day('2022-06-22')):      return 6867
        if (sim.t>=sim.day('2022-06-22'))*(sim.t < sim.day('2022-07-22')):      return 6124
        if (sim.t>=sim.day('2022-07-22'))*(sim.t < sim.day('2022-08-22')):      return 4147
        if (sim.t>=sim.day('2022-08-22'))*(sim.t < sim.day('2022-09-22')):      return 2772
        if (sim.t>=sim.day('2022-09-22'))*(sim.t < sim.day('2022-10-22')):      return 4664
        if (sim.t>=sim.day('2022-10-22'))*(sim.t < sim.day('2022-11-22')):      return 3670
        if (sim.t>=sim.day('2022-11-22'))*(sim.t < sim.day('2023-01-01')):      return 1338
        else:                                                  return 0  
        
    def num_boosters2(sim):
        if sim.t < sim.day('2022-03-22'):                      return 0
        if (sim.t>=sim.day('2022-03-22'))*(sim.t < sim.day('2022-04-22')):      return 65162
        if (sim.t>=sim.day('2022-04-22'))*(sim.t < sim.day('2022-05-22')):      return 45822
        if (sim.t>=sim.day('2022-05-22'))*(sim.t < sim.day('2022-06-22')):      return 14614
        if (sim.t>=sim.day('2022-06-22'))*(sim.t < sim.day('2022-07-22')):      return 6065
        if (sim.t>=sim.day('2022-07-22'))*(sim.t < sim.day('2022-08-22')):      return 1509
        if (sim.t>=sim.day('2022-08-22'))*(sim.t < sim.day('2022-09-22')):      return 137
        else:                                                  return 0
        
    def num_boosters3(sim):
        if sim.t < sim.day('2022-09-01'):                      return 0
        if (sim.t>=sim.day('2022-09-01'))*(sim.t < sim.day('2022-10-01')):      return 146885
        if (sim.t>=sim.day('2022-10-01'))*(sim.t < sim.day('2022-11-01')):      return 229941
        if (sim.t>=sim.day('2022-11-01'))*(sim.t < sim.day('2022-12-01')):      return 95047
        if (sim.t>=sim.day('2022-12-01'))*(sim.t < sim.day('2023-01-01')):      return 16097
        else:                                                  return 0
     
    def num_boosters4(sim):
        if sim.t < sim.day('2022-09-01'):                      return 0
        if (sim.t>=sim.day('2022-09-01'))*(sim.t < sim.day('2023-01-01')):      return 10000
        else:                                                  return 0
    
    
    if booster_ind == 1:
        booster = cv.vaccinate_num(vaccine=booster, label='booster', 
                                   sequence='age', subtarget=booster_target, 
                                   num_doses=num_boosters, booster=True)
        interventions += [booster]
        
    elif booster_ind == 2:
        booster = cv.vaccinate_num(vaccine=booster, label='booster', 
                                   sequence='age', subtarget=booster_target, 
                                   num_doses=num_boosters, booster=True)
        booster2 = cv.vaccinate_num(vaccine=booster2, label='booster2', 
                                    sequence='age', subtarget=booster_target2, 
                                    num_doses=num_boosters2, booster=True)
        interventions += [booster]
        interventions += [booster2]
        
    elif booster_ind == 3:
        booster = cv.vaccinate_num(vaccine=booster, label='booster', 
                                   sequence='age', subtarget=booster_target, 
                                   num_doses=num_boosters, booster=True)
        booster2 = cv.vaccinate_num(vaccine=booster2, label='booster2', 
                                    sequence='age', subtarget=booster_target2, 
                                    num_doses=num_boosters2, booster=True)
        booster3 = cv.vaccinate_num(vaccine=booster3, label='booster3', 
                                    sequence='age', subtarget=booster_target3, 
                                    num_doses=num_boosters3, booster=True)
        interventions += [booster]
        interventions += [booster2]
        interventions += [booster3]
        
    elif booster_ind == 4:
        booster = cv.vaccinate_num(vaccine=booster, label='booster', 
                                   sequence='age', subtarget=booster_target, 
                                   num_doses=num_boosters, booster=True)
        booster2 = cv.vaccinate_num(vaccine=booster2, label='booster2', 
                                    sequence='age', subtarget=booster_target2, 
                                    num_doses=num_boosters2, booster=True)
        booster3 = cv.vaccinate_num(vaccine=booster3, label='booster3', 
                                    sequence='age', subtarget=booster_target3, 
                                    num_doses=num_boosters3, booster=True)
        booster4 = cv.vaccinate_num(vaccine=booster4, label='booster4', 
                                    subtarget=booster_target4, 
                                    num_doses=num_boosters4, booster=True)
        interventions += [booster]
        interventions += [booster2]
        interventions += [booster3]
        interventions += [booster4]
        
    
    # Finally, update the parameters
    sim.update_pars(interventions=interventions, variants=variants)
    for intervention in sim['interventions']:
        intervention.do_plot = False
        
# =============================================================================
#     age_stats = cv.daily_age_stats(states=['infectious', 'severe', 'critical', 'dead'], edges = [0,5,12 ,16 ,18 ,25 ,30 ,35 ,40 ,45 ,50 ,55 ,60 ,65 ,70 ,75 ,80 ,85 ,90])
#     analyzers = [age_stats]    
#     sim.update_pars(analyzers=analyzers)
# =============================================================================

    sim.initialize()
    return sim

if __name__ == '__main__':

# =============================================================================
# using analyzers to look at the infections, hospitalisations, deaths etc, in just the adolescent population

    #final_median = pd.DataFrame()
    #final_25 = pd.DataFrame()
    #final_75 = pd.DataFrame()
    #final_0 = pd.DataFrame()
    #final_100 = pd.DataFrame()
    #severe_booster = pd.DataFrame()
    #critical_booster = pd.DataFrame()
    #dead_booster = pd.DataFrame()
    #for j2 in []:
    #    final_median_0 = pd.DataFrame()
    #    final_25_0 = pd.DataFrame()
    #    final_75_0 = pd.DataFrame()
    #    final_0_0 = pd.DataFrame()
    #    final_100_0 = pd.DataFrame()
    #    
    #    final_median_1 = pd.DataFrame()
    #    final_25_1 = pd.DataFrame()
    #    final_75_1 = pd.DataFrame()
    #    final_0_1 = pd.DataFrame()
    #    final_100_1 = pd.DataFrame()
    # 
    #    final_median_2 = pd.DataFrame()
    #    final_25_2 = pd.DataFrame()
    #    final_75_2 = pd.DataFrame()
    #    final_0_2 = pd.DataFrame()
    #    final_100_2 = pd.DataFrame()
    #    
    #    values_0 = pd.DataFrame()
    #    values_1 = pd.DataFrame()
    #    values_2 = pd.DataFrame()
    #    for x in range(2):
    #        sim = create_sim(0,j2,4,3, with_omicron=1)
    #        sim = sim.copy()
    #        sim['rand_seed'] = x
    #        sim.set_seed()
    #        sim.set_seed(seed = x)
    #        sim.label = f"Sim {x, j2}"
    #        age_stats = cv.daily_age_stats(states = ['cum_severe','cum_critical','cum_dead'],edges = [12,18])
    #        analyzers = [age_stats]    
    #        sim.update_pars(analyzers=analyzers)
    #        sim.initialize()
    #        sim.run()
    #        agehist = sim.get_analyzer()
    #        x1 = agehist.results    
    #        dates = [datetime.datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in x1.keys()]
    #        values_new_sev =  pd.DataFrame(np.array([list(value.values())[0] for _, value in agehist.results.items()]))
    #        values_new_cri =  pd.DataFrame(np.array([list(value.values())[1] for _, value in agehist.results.items()]))
    #        values_new_dea =  pd.DataFrame(np.array([list(value.values())[2] for _, value in agehist.results.items()]))
    #        values_0 = pd.concat([values_0,values_new_sev[:][[0]]],axis = 1)
    #        values_1 = pd.concat([values_1,values_new_cri[:][[0]]],axis = 1)
    #        values_2 = pd.concat([values_2,values_new_dea[:][[0]]],axis = 1)
    #    final_median_0 = pd.concat([final_median_0,values_0.median(axis=1)], axis = 1)
    #    final_25_0 = pd.concat([final_25_0,values_0.quantile(0.25,axis=1)], axis = 1)
    #    final_75_0 = pd.concat([final_75_0,values_0.quantile(0.75,axis=1)], axis = 1)
    #    final_0_0 = pd.concat([final_0_0,values_0.quantile(0,axis=1)], axis = 1)
    #    final_100_0 = pd.concat([final_100_0,values_0.quantile(1,axis=1)], axis = 1)
    #    
    #    final_median_1 = pd.concat([final_median_1,values_1.median(axis=1)], axis = 1)
    #    final_25_1 = pd.concat([final_25_1,values_1.quantile(0.25,axis=1)], axis = 1)
    #    final_75_1 = pd.concat([final_75_1,values_1.quantile(0.75,axis=1)], axis = 1)
    #    final_0_1 = pd.concat([final_0_1,values_1.quantile(0,axis=1)], axis = 1)
    #    final_100_1 = pd.concat([final_100_1,values_1.quantile(1,axis=1)], axis = 1)
    #    
    #    final_median_2 = pd.concat([final_median_2,values_2.median(axis=1)], axis = 1)
    #    final_25_2 = pd.concat([final_25_2,values_2.quantile(0.25,axis=1)], axis = 1)
    #    final_75_2 = pd.concat([final_75_2,values_2.quantile(0.75,axis=1)], axis = 1)
    #    final_0_2 = pd.concat([final_0_2,values_2.quantile(0,axis=1)], axis = 1)
    #    final_100_2 = pd.concat([final_100_2,values_2.quantile(1,axis=1)], axis = 1)
    #            
    #    severe_booster = pd.concat([severe_booster,final_25_0,final_median_0,final_75_0],axis=1)
    #    critical_booster = pd.concat([critical_booster,final_25_1,final_median_1,final_75_1],axis=1)       
    #    dead_booster = pd.concat([dead_booster,final_25_2,final_median_2,final_75_2],axis=1)
    #    
    #    
    #    
    #sev_booster = pd.concat([pd.Series(dates),severe_booster],axis=1)
    #cri_booster = pd.concat([pd.Series(dates),critical_booster],axis=1)
    #dea_booster = pd.concat([pd.Series(dates),dead_booster],axis=1)
    #sev_booster.columns = ['Date','No_AB_25','No_AB_med','No_AB_75',
    #                     'AB_25','AB_med','AAB_75']
    #cri_booster.columns = ['Date','No_AB_25','No_AB_med','No_AB_75',
    #                     'AB_25','AB_med','AAB_75']
    #dea_booster.columns = ['Date','No_AB_25','No_AB_med','No_AB_75',
    #                     'AB_25','AB_med','AAB_75']
    #
    #sev_booster.columns = ['Date','0%_25','0%_med','0%_75',
    #                     '50%_25','50%_med','50%_75','70%_25','70%_med','70%_75','90%_25','90%_med','90%_75']
    #cri_booster.columns = ['Date','0%_25','0%_med','0%_75',
    #                     '50%_25','50%_med','50%_75','70%_25','70%_med','70%_75','90%_25','90%_med','90%_75']
    #dea_booster.columns = ['Date','0%_25','0%_med','0%_75',
    #                     '50%_25','50%_med','50%_75','70%_25','70%_med','70%_75','90%_25','90%_med','90%_75']
    #    
    #    
    #sev_booster.to_excel('sev_adolescent_4.xlsx')   
    #cri_booster.to_excel('cri_adolescent_4.xlsx')   
    #dea_booster.to_excel('dea_adolescent_4.xlsx')   

# =============================================================================

# =============================================================================
    
    with_omicron = 1
    
    sim = create_sim(0,0,0,3, with_omicron = 1) # baseline scenario
    #sim = create_sim(0,10,6,3, with_omicron = 0) # no omicron scenario
    sims = []
    for seed in range(30):
        sim = sim.copy()
        sim['rand_seed'] = seed
        sim.set_seed()
        sim.set_seed(seed=seed)
        sim.label = f"Sim {seed}"
        sims.append(sim)
    # multisim running
    msim = cv.MultiSim(sims)
    msim.run(keep_people = 0)    
    msim.reduce([0.25,0.75]) # use msim.reduce([0.05,0.95]) to find the upper and lower values for the box plot figures
    
    # for the 3D plot: saving each run as __.xlsx where the first _ is (a,b,c,d,e,f) 
    # and corresponds to when vaccination starts from with day_start = 0 for a, 
    # day_start = 1 for b etc. and the second _ is one of (a,b,c,d,e,f,g,h,i,j) and 
    # corresponds to adolescent vaccine percentage with per_vac = 0 (i.e. 0%) for a, 
    # per_vac = 1 (i.e.10%) for b and per_vac = 2 (i,e, 20%) for c, so that a file 
    # called cd.xlsx corresponds to a vaccine start that is 4 weeks delayed from the 
    # first vaccine rollout date scenario, and approx 30% of adolescents are being vaccinated 
    
    
    #msim.to_excel('aa.xlsx')
    #msim.to_excel('ba.xlsx')
    #msim.to_excel('ca.xlsx')
    #msim.to_excel('da.xlsx')
    #msim.to_excel('ea.xlsx')
    #msim.to_excel('fa.xlsx')
    #msim.to_excel('ab.xlsx')
    #msim.to_excel('bb.xlsx')
    #msim.to_excel('cb.xlsx')
    #msim.to_excel('db.xlsx')
    #msim.to_excel('eb.xlsx')
    #msim.to_excel('fb.xlsx')
    #msim.to_excel('ac.xlsx')
    #msim.to_excel('bc.xlsx')
    #msim.to_excel('cc.xlsx')
    #msim.to_excel('dc.xlsx')
    #msim.to_excel('ec.xlsx')
    #msim.to_excel('fc.xlsx')
    #msim.to_excel('ad.xlsx')
    #msim.to_excel('bd.xlsx')
    #msim.to_excel('cd.xlsx')
    #msim.to_excel('dd.xlsx')
    #msim.to_excel('ed.xlsx')
    #msim.to_excel('fd.xlsx')
    #msim.to_excel('ae.xlsx')
    #msim.to_excel('be.xlsx')
    #msim.to_excel('ce.xlsx')
    #msim.to_excel('de.xlsx')
    #msim.to_excel('ee.xlsx')
    #msim.to_excel('fe.xlsx')
    #msim.to_excel('af.xlsx')
    #msim.to_excel('bf.xlsx')
    #msim.to_excel('cf.xlsx')
    #msim.to_excel('df.xlsx')
    #msim.to_excel('ef.xlsx')
    #msim.to_excel('ff.xlsx')
    #msim.to_excel('ag.xlsx')
    #msim.to_excel('bg.xlsx')
    #msim.to_excel('cg.xlsx')
    #msim.to_excel('dg.xlsx')
    #msim.to_excel('eg.xlsx')
    #msim.to_excel('fg.xlsx')
    #msim.to_excel('ah.xlsx')
    #msim.to_excel('bh.xlsx')
    #msim.to_excel('ch.xlsx')
    #msim.to_excel('dh.xlsx')
    #msim.to_excel('eh.xlsx')
    #msim.to_excel('fh.xlsx')
    #msim.to_excel('ai.xlsx')
    #msim.to_excel('bi.xlsx')
    #msim.to_excel('ci.xlsx')
    #msim.to_excel('di.xlsx')
    #msim.to_excel('ei.xlsx')
    #msim.to_excel('fi.xlsx')
    #msim.to_excel('aj.xlsx')
    #msim.to_excel('bj.xlsx')
    #msim.to_excel('cj.xlsx')
    #msim.to_excel('dj.xlsx')
    #msim.to_excel('ej.xlsx')
    #msim.to_excel('fj.xlsx')
    
# =============================================================================
    
    daily_diagnoses = sc.objdict({
         'Baseline Scenario: Daily Number of Covid-19 Diagnoses': ['new_diagnoses']})
    
    cumulative_diagnoses = sc.objdict({
        'Baseline Scenario: Cumulative Number of Covid-19 Diagnoses': ['cum_diagnoses']})
    
    daily_infectious = sc.objdict({
         'Baseline Scenario: Daily Number of Infectious People': ['new_infectious']})
    
    daily_infections = sc.objdict({
         'Baseline Scenario: Daily Number of New Infections': ['new_infections']})
    
    cumulative_infectious = sc.objdict({
         'Baseline Scenario: Cumulative Number of Infectious People': ['cum_infectious']})
    
    cumulative_infections = sc.objdict({
         'Baseline Scenario: Cumulative Number of New Infections': ['cum_infections']})
    
    daily_diagnoses_2 = sc.objdict({
         'Daily Number of Covid-19 Diagnoses': ['new_diagnoses']})
    
    cumulative_diagnoses_2 = sc.objdict({
        'Cumulative Number of Covid-19 Diagnoses': ['cum_diagnoses']})
    
    daily_infectious_2 = sc.objdict({
         'Daily Number of Infectious People': ['new_infectious']})
    
    cumulative_infectious_2 = sc.objdict({
         'Cumulative Number of Infectious People': ['cum_infectious']})
    
    new_tests = sc.objdict({
         'Baseline Scenario: Daily Number of Tests': ['new_tests']})
    
    daily_hospitalisations = sc.objdict({
         'Baseline Scenario: Daily Number of Hospitalisations due to Covid-19': ['new_severe']})
    
    daily_ICUs = sc.objdict({
         'Baseline Scenario: Daily Number of Hospitalisations (ICUs)': ['new_critical']})
    
    daily_deaths = sc.objdict({
         'Baseline Scenario: Daily Number of Deaths due to Covid-19': ['new_deaths']})
    
    cumulative_hospitalisations = sc.objdict({
         'Baseline Scenario: Cumulative Number of Hospitalisations due to Covid-19': ['cum_severe']})
    
    cumulative_ICUs = sc.objdict({
         'Baseline Scenario: Cumulative Number of Hospitalisations (ICUs)': ['cum_critical']})
    
    cumulative_deaths = sc.objdict({
         'Baseline Scenario: Cumulative Number of Deaths due to Covid-19': ['cum_deaths']})
    
    daily_hospitalisations_2 = sc.objdict({
         'Daily Number of Hospitalisations due to Covid-19': ['new_severe']})
    
    daily_ICUs_2 = sc.objdict({
         'Daily Number of Hospitalisations (ICUs)': ['new_critical']})
    
    daily_deaths_2 = sc.objdict({
         'Daily Number of Deaths due to Covid-19': ['new_deaths']})
    
    cumulative_hospitalisations_2 = sc.objdict({
         'Cumulative Number of Hospitalisations due to Covid-19': ['cum_severe']})
    
    cumulative_ICUs_2 = sc.objdict({
         'Cumulative Number of Hospitalisations (ICUs)': ['cum_critical']})
    
    cumulative_deaths_2 = sc.objdict({
         'Cumulative Number of Deaths due to Covid-19': ['cum_deaths']})
    
    prevalence = sc.objdict({
         'Baseline Scenario: Prevalence': ['prevalence']})
    
    incidence = sc.objdict({
         'Baseline Scenario: Incidence': ['incidence']})
    
    R_number = sc.objdict({
         'Baseline Scenario: Effective Reproduction Number': ['r_eff']})
    
    cumulative_vaccinated = sc.objdict({
         'Baseline Scenario: Cumulative Number of Vaccinated People (at least one dose)': ['cum_vaccinated']})
    
    daily_infectious_by_variant = sc.objdict({
         'Baseline Scenario: Daily Number of Infectious People by Variant': ['new_infectious_by_variant']})
    
    daily_infections_by_variant = sc.objdict({
         'Baseline Scenario: Daily Number of New Infections by Variant': ['new_infections_by_variant']})
    
# =============================================================================
   
 
    
    
# =============================================================================

# Baseline Scenario figures

# Figure 3g)
#    msim.plot(to_plot = daily_infectious, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'new_infectious'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3a)    
#    msim.plot(to_plot = daily_hospitalisations, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'new_severe'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3c)    
#    msim.plot(to_plot = daily_ICUs, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'new_critical'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Appendix figure    
#    msim.plot(to_plot = daily_deaths, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'new_deaths'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3e)    
#    msim.plot(to_plot = daily_diagnoses, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'new_diagnoses'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3h)    
#    msim.plot(to_plot = cumulative_infectious, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'cum_infectious'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3b)    
#    msim.plot(to_plot = cumulative_hospitalisations, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'cum_severe'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3d)    
#    msim.plot(to_plot = cumulative_ICUs, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'cum_critical'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# Figure 3f)    
#    msim.plot(to_plot = cumulative_deaths, style='bmh', do_save = True, do_show = False, 
#                    tight = True, fig_args = {'num':'cum_deaths'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
#   
#    msim.plot(to_plot = cumulative_diagnoses, style='bmh', do_save = False, do_show = False, 
#                    tight = True, fig_args = {'num':'cum_diagnoses'}, 
#                    start = '2020-01-20', end = '2023-04-30', commaticks = True, 
#                    figsize = (8,4), dpi = 150, fontsize = 9)
# =============================================================================
    

# =============================================================================

## Figures 2
# Figure 2b)
#    colors = sc.gridcolors(ncolors=10)
#
#    colors_dict = {'wild type': colors[0],'Alpha':colors[1], 'Delta':colors[2], 'Omicron BA.1':colors[3],
#                   'B.1.177':colors[4],
#                   'Omicron BA.1.1':colors[5],
#                   'Omicron BA.2':colors[6],
#                   'Omicron BA.4':colors[7], 
#                   'Omicron BA.5':colors[8],
#                   'Omicron XBB':colors[9]}
#    
#    daily_infectious_by_variant = sc.objdict({
#        'Baseline Scenario: Daily Number of Infectious People by Variant': ['new_infectious_by_variant']})
#    
# 
#    data = pd.read_excel('test_1.xlsx') # whatever file name the baseline scenario is called
#    msim.plot(to_plot = daily_infectious_by_variant, style='bmh', do_save = False, do_show = False, 
#                   tight = True, fig_args = {'num':'new_infectious_by_variant'}, 
#                   start = '2020-09-01', end = end_day, 
#                   figsize = (10,4), dpi = 150, legend_args = {'loc': 'center right', 'bbox_to_anchor': (1.35, 0.5)}, fontsize = 9)
#    ax=pl.gca()
#    ax.set_ylim([0,600000])
#    ax.plot(data.date, data.new_infectious, color = 'black', alpha = 0.7, linewidth = 0.5)
#    ax.axvline(x=data.date[581], color = 'black', linewidth=0.8, ls='--')
#    ax.axvline(x=data.date[609], color = 'black', linewidth=0.8, ls='--')
#    ax.axvline(x=data.date[665], color = 'black', linewidth=0.8, ls='--')
#    ax.axvline(x=data.date[693], color = 'black', linewidth=0.8, ls='--')
#    trans = ax.get_xaxis_transform()
#    
#         
#    ax.text(data.date[568], .5, '1st vaccine for ages 16-17', transform = trans, rotation = 90, fontsize = 6)
#    ax.text(data.date[596], .5, '1st vaccine for ages 12-15', transform = trans, rotation = 90, fontsize = 6)
#    ax.text(data.date[652], .5, '2nd vaccine for ages 16-17', transform = trans, rotation = 90, fontsize = 6)
#    ax.text(data.date[680], .5, '2nd vaccine for ages 12-15', transform = trans, rotation = 90, fontsize = 6)
#    ax2=ax.twinx()
#    ax2.set_ylim([0,2.5])
#    ax2.grid(False)
#    ax2.plot(data.date, data.r_eff, color='blue', alpha = 0.1, label = 'R number')
#    ax2.plot(data.date, data.r_eff_low, color='blue', alpha = 0)
#    ax2.plot(data.date, data.r_eff_high, color='blue', alpha = 0)
#    ax2.fill_between(data.date, data.r_eff_low, data.r_eff_high, alpha = 0.1, color = 'blue')
#    ax2.legend(framealpha = 0, loc = 'lower right', bbox_to_anchor = (1.2855, 0.085))
#    pl.box(False)
#    pl.savefig('Figure_1.png')
# 
# Figure 2a)    
#    var4 = pd.read_excel('proportion_england.xlsx', skiprows=2)
#    base = datetime.date(2020,9,5)
#    x4 = [base + datetime.timedelta(days=7*x) for x in range(129)]
#    #y4_1 = list(var4['A'])
#    y4_2 = list(var4['B'])
#    y4_3 = list(var4['B.1.1.529'])
#    y4_4 = list(var4['B.1.1.7'])
#    y4_5 = list(var4['B.1.617.2'])
#    y4_6 = list(var4['BA.1.1'])
#    y4_7 = list(var4['BA.2'])
#    y4_8 = list(var4['BA.4'])
#    y4_9 = list(var4['BA.5'])
#    
#    fig7 = pl.figure(figsize = (10,4),dpi = 150)
#    
#    #colors2 = ['#CBD6E2', '#F07857', '#43A5BE', '#F5C23B', '#253342', '#53BDA5', '#EBB8DD', '#BF23C4', '#0033FF']
#    pl.stackplot(x4,[y4_2, y4_4, y4_5, y4_3, y4_6, y4_7, y4_8, y4_9], colors=colors[1:9],
#                 labels = ['B.1.177', 'Alpha', 'Delta', 'BA.1', 'BA.1.1', 'BA.2', 'BA.4', 'BA.5'])
#    sc.dateformatter(ax=pl.gca(), style='sciris', dateformat = '%b', start = start_day, end = end_day)
#    pl.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,5,9)))
#    pl.gca().set_xlabel('Date')
#    pl.gca().set_ylabel('Proportion (%)')
#    pl.gca().set_title('Estimated Proportion of Infections Belonging to Each Variant')
#    pos = pl.gca().get_position()
#    pl.gca().set_position([pos.x0, pos.y0, pos.width * 0.9, pos.height])
#    pl.gca().legend(loc='center right', bbox_to_anchor=(1.17, 0.5), framealpha=0)
#    pl.gca().set_xlim([datetime.date(2020,9,5), datetime.date(2023,1,1)])
#    pl.gca().set_ylim([0,100])
#    pl.savefig('variants_proportion_data.png')
#    
# =============================================================================

# =============================================================================

# No Omicron scenario figures 



    if with_omicron == 0:
        
        
        sim = create_sim(0,0,0,3, with_omicron = 0) # no omicron scenario
        sims = []
        for seed in range(30):
            sim = sim.copy()
            sim['rand_seed'] = seed
            sim.set_seed()
            sim.set_seed(seed=seed)
            sim.label = f"Sim {seed}"
            sims.append(sim)
            
        
        # multisim running
        msim = cv.MultiSim(sims)
        msim.run(keep_people = 0)
        
        msim.reduce([0.25,0.75])
        
        msim.plot(to_plot = daily_infectious_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_1.png', do_show = False, 
                       tight = True, fig_args = {'num':'new_infectious'}, 
                       start = '2021-05-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Daily Number of Infectious People',
                       legend_args = {'show_legend': False})    
        data = pd.read_excel('test_1.xlsx') # insert name for whatever .xlsx file you save the baseline scenario as
        pl.gca().set_ylim([0, 700000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.new_infectious[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.new_infectious_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.new_infectious_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.new_infectious_low[590:950], 
                             data.new_infectious_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_1.png')

             
        msim.plot(to_plot = cumulative_infectious_2, style='bmh', do_save = True, 
                      fig_path = 'no_Omicron_2.png', do_show = False, 
                       tight = True, fig_args = {'num':'cum_infectious'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Cumulative Number of Infectious People',
                       legend_args = {'show_legend': False})
        pl.gca().set_ylim([20000000, 70000000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.cum_infectious[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.cum_infectious_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.cum_infectious_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.cum_infectious_low[590:950], 
                                  data.cum_infectious_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_2.png')
        
        msim.plot(to_plot = daily_hospitalisations_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_3.png', do_show = False, 
                       tight = True, fig_args = {'num':'new_severe'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Daily Number of Hospitalisations',
                       legend_args = {'show_legend': False}, colors = '#e33d3e')
        pl.gca().set_ylim([0, 4000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.new_severe[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.new_severe_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.new_severe_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.new_severe_low[590:950], 
                                  data.new_severe_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_3.png')

        msim.plot(to_plot = cumulative_hospitalisations_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_4.png', do_show = False, 
                       tight = True, fig_args = {'num':'cum_severe'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Cumulative Number of Hospitalisations',
                       legend_args = {'show_legend': False}, colors = '#e33d3e')
        pl.gca().set_ylim([400000, 700000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.cum_severe[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.cum_severe_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.cum_severe_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.cum_severe_low[590:950], 
                                   data.cum_severe_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_4.png')
        
        msim.plot(to_plot = daily_deaths_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_5.png', do_show = False, 
                       tight = True, fig_args = {'num':'cum_deaths'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Daily Number of Deaths',
                       legend_args = {'show_legend': False}, colors = '#e33d3e')
        ax=pl.gca()
        ax.plot(data.date[590:950], data.cum_deaths[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.cum_deaths_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.cum_deaths_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.cum_deaths_low[590:950], 
                                   data.cum_deaths_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_5.png')

        msim.plot(to_plot = cumulative_deaths_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_6.png', do_show = False, 
                       tight = True, fig_args = {'num':'cum_deaths'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Cumulative Number of Deaths',
                       legend_args = {'show_legend': False}, colors = '#e33d3e')
        pl.gca().set_ylim([110000, 160000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.cum_deaths[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.cum_deaths_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.cum_deaths_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.cum_deaths_low[590:950], 
                                   data.cum_deaths_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_6.png')
           
        msim.plot(to_plot = daily_diagnoses_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_7.png', do_show = False, 
                       tight = True, fig_args = {'num':'new_diagnoses'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Daily Number of Diagnoses',
                       legend_args = {'show_legend': False}, colors='#e33d3e')
        pl.gca().set_ylim([0, 190000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.new_diagnoses[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.new_diagnoses_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.new_diagnoses_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.new_diagnoses_low[590:950], 
                                   data.new_diagnoses_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_7.png')
            
        msim.plot(to_plot = cumulative_diagnoses_2, style='bmh', do_save = True, 
                       fig_path = 'no_Omicron_8', do_show = False, 
                       tight = True, fig_args = {'num':'cum_diagnoses'}, 
                       start = '2021-09-01', end = '2022-03-01', commaticks = True, 
                       figsize = (8,4), dpi = 150, labels = 'Cumulative Number of Diagnoses',
                       legend_args = {'show_legend': False}, colors = '#e33d3e')
        pl.gca().set_ylim([5000000, 17500000])
        ax=pl.gca()
        ax.plot(data.date[590:950], data.cum_diagnoses[590:950], color = 'blue', label = 'With Omicron', alpha = 1)
        ax.plot(data.date[590:950], data.cum_diagnoses_low[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.plot(data.date[590:950], data.cum_diagnoses_high[590:950], color = 'blue', linewidth = 0.0025, alpha = 0.5)
        ax.fill_between(data.date[590:950], data.cum_diagnoses_low[590:950], 
                                  data.cum_diagnoses_high[590:950], alpha = 0.15, color = 'blue')
        handles, labels = ax.get_legend_handles_labels()
        labels[0] = 'Without Omicron'
        ax.legend(handles=handles, labels=labels, loc = 'upper left')
        pl.savefig('no_Omicron_8.png')
        
# =============================================================================


        # sim = create_sim(0,10,6,4)
        # n_doses = []
        # dose_analyzer   = lambda msim: n_doses.append(msim.people.doses.copy())
        # age_stats       = cv.daily_age_stats(states=['vaccinated', 'exposed', 'severe', 'dead'], edges = [0,5,12 ,16 ,18 ,25 ,30 ,35 ,40 ,45 ,50 ,55 ,60 ,65 ,70 ,75 ,80 ,85 ,90])
        # analyzers       = [dose_analyzer, age_stats]    
        # sim.update_pars(analyzers=analyzers)
        # sim.initialize()
        # pop_scale = int(55.98e6/100e3)
        # sim.run()
        # daily_age = sim.get_analyzer(1)
        
        # x = daily_age.results
        # length = len(list(x.items()))
        # list_temp = list(x.items()[0])
        # date_temp = list_temp[0]
        # value_temp = list_temp[1]
        # value_temp2 = list(value_temp.items())
        # value_temp3 = value_temp2[0]
        # values_temp = value_temp3[1]
        # date = []
        # date += [date_temp]
        # values = values_temp
        
        # for i in range(length-1):
        #     list_temp = list(x.items()[i+1])
        #     date_temp = list_temp[0]
        #     value_temp = list_temp[1]
        #     value_temp2 = list(value_temp.items())
        #     value_temp3 = value_temp2[0]
        #     values_temp = value_temp3[1]
        #     date += [date_temp]
        #     values = np.column_stack((values, values_temp))
        
        # dates = []
        # for i in range(length):
        #     date_ = datetime.strptime(date[0], '%Y-%m-%d').date()
        #     dates.append(date_)
        
        # pl.style.use('ggplot')
        
        # # Vaccination Time Series Plot
        
        # pl.figure(figsize = (10,4), dpi = 150, num = 'vaccination_time_series')
        
        # dataframe = pd.DataFrame({'Date': np.array([dt.datetime(2020, 1, 20)+dt.timedelta(days=i)
        #                                                 for i in range(length)])})
        # dataframe1 = pd.DataFrame({'Date': np.array([dt.datetime(2020, 3, 1)+dt.timedelta(days=i)
        #                                                 for i in range(len(losses_sev[0]))])})
       
        # ages = [5,12,16,18,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
        # colors = sc.vectocolor(len(ages), cmap='viridis')
        
        # for i in range(len(ages)):
        #     pl.plot(dataframe.Date, values[i], c = colors[i])
        
        # pl.rc({'font_size': 10})
        # pl.ylim(0,550000)
        # pl.xlim(18281,18281+length)
        # ax = pl.gca()
        # ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
        # pl.xlabel('Date')
        # pl.ylabel('Number of Vaccinations')
        # pl.legend(['Age 5-11', 'Age 12-15','Age 16-17', 'Age 18-24', 'Age 25-29', 'Age 30-34', 
        #            'Age 35-39', 'Age 40-44', 'Age 45-49', 'Age 50-54', 'Age 55-59', 
        #            'Age 60-64', 'Age 65-69', 'Age 70-74', 'Age 75-79', 'Age 80-84', 
        #            'Age 85-89', 'Age 90+'], prop={'size': 8}, framealpha = 0)
        # pl.title('Baseline Scenario: Time Series of Vaccinations Per Age Group')
        # sc.dateformatter(ax=pl.gca(), style='sciris', dateformat = '%b', start = start_day, end = end_day)
        # pl.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,5,9)))
        # pl.savefig('baseline_vaccination_time_series.png')
        
        
        # daily_age.plot(total=True, color = '#63C5DA', width = 0.1, 
        #                style_args = {'fontsize': 8}, grid = False, 
        #                plot_args = {'supylabel':'Number of Vaccinations', 'tight':True},
        #                style='ggplot')
        
        # # age histogram
        # pl.figure(figsize = (10,5), dpi = 150, num = 'age_distribution')
        # people=sim.people
        # alpha = 0.6
        # bins = [0,5,12,16,18,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
        # width = 1
        # color     = [0.1,0.1,0.1] 
        # n_rows    = 4 
        # offset    = 0.5 
        # gridspace = 10 
        # zorder    = 10 
        # min_age = min(bins)
        # max_age = max(bins)
        # edges = np.append(bins, np.inf) 
        # age_counts = 560*np.histogram(people.age, edges)[0]
        # pl.gca().grid(True, zorder = 0)
        # pl.bar(bins+np.array([2.6,3.6,2.1,1.1,3.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,5.1]), 
        #        age_counts/np.array([5,7,4,2,7,5,5,5,5,5,5,5,5,5,5,5,5,5,10]), alpha = 1, color='#355E3B',  width = [4.8,6.8,3.8,1.8,6.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,9.8], zorder = 5)
        # pl.xlim([0,100])
        # pl.xticks(bins+[100])
        # pl.xlabel('Age')
        # pl.ylabel('Population Density')
        # pl.title('Population Age Histogram')
        # ax = pl.gca()
        # ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
        # pl.grid(False, axis = 'x')
        # pl.xticks(fontsize = 8)
        # pl.savefig('age_distribution.png')
        
        # vaccinated_age=[]
        # for i in range(len(people.vaccinated)):
        #     if people.vaccinated[i] == True:
        #         vaccinated_age += [people.age[i]]
                
          
        # # vaccine final uptake
            
        # pl.figure(figsize = (10,5), dpi = 150, num = 'vaccine_distribution')
        # people=sim.people
        # alpha = 0.6
        # bins = [0,5,12,16,18,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
        # width = 1
        # color     = [0.1,0.1,0.1]
        # n_rows    = 4 
        # offset    = 0.5 
        # gridspace = 10
        # zorder    = 10
        # min_age = min(bins)
        # max_age = max(bins)
        # edges = np.append(bins, np.inf) 
        # age_counts2 = 560*np.histogram(vaccinated_age, edges)[0]
        # pl.gca().grid(True, zorder = 0)
        # pl.bar(bins+np.array([2.5,3.5,2, 1, 3.5, 2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,5]), 
        #        age_counts2/age_counts, alpha = 1, color='#A94064',  width = 0.5, zorder = 5)
        # pl.xlim([0,100])
        # pl.xticks(bins+[100])
        # pl.xlabel('Age')
        # pl.ylabel('Vaccine Uptake')
        # pl.title('Baseline Scenario: Vaccine Uptake by Age Group')
        # ax = pl.gca()
        # pl.grid(False, axis = 'x')
        # pl.xticks(fontsize = 8)
        # pl.savefig('baseline1_vaccine_distribution.png')
        
        
        # # cumulative number of vaccinations by dose plot
        # pl.figure(figsize = (10,4), dpi = 150)
        # n_doses = np.array(n_doses)
        # fully_vaccinated = (n_doses == 2).sum(axis=1)*pop_scale
        # first_dose = (n_doses == 1).sum(axis=1)*pop_scale
        # boosted1 = (n_doses == 3).sum(axis=1)*pop_scale
        # boosted2 = (n_doses > 3).sum(axis=1)*pop_scale
        # pal = sns.color_palette('Set2')
        # ax=pl.gca()
        # ax.grid(True, zorder=0)
        # #ax.set_facecolor('#f2f2ff')
        # pl.stackplot(dataframe.Date, [first_dose, fully_vaccinated, boosted1, boosted2], colors = pal, alpha = 1, zorder = 5)
        # pl.legend(['First dose', 'Second Dose', 'Boosted x1', 'Boosted x2'], loc = 'upper left', framealpha = 0)
        # ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
        # pl.xlabel('Date')
        # pl.ylabel('Number of Vaccinated People')
        # pl.title('Baseline Scenario: Cumulative Number of Vaccinated People Per Dose')
        # sc.dateformatter(ax=pl.gca(), style='sciris', dateformat = '%b', start = start_day, end = end_day)
        # pl.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,5,9)))
        # pl.xlim(18281,18281+length-1)
        # pl.gca().set_ylim([0, 40000000])
        # pl.savefig('baseline1_vaccinated_per_dose.png')

       

### infections by adolescents for different adolescent vaccination strategies

    # final_median = pd.DataFrame()
    # final_25 = pd.DataFrame()
    # final_75 = pd.DataFrame()
    # final_0 = pd.DataFrame()
    # final_100 = pd.DataFrame()
        
    # for j2 in [0,2,4]:
    #     final_median = pd.DataFrame()
    #     final_25 = pd.DataFrame()
    #     final_75 = pd.DataFrame()
    #     final_0 = pd.DataFrame()
    #     final_100 = pd.DataFrame()
    #     for j in [0,5,7,9]:
    #         values_0 = pd.DataFrame()
    #         for x in range(30):
    #             sim = create_sim(x,j,j2,3)
    #             sim = sim.copy()
    #             sim['rand_seed'] = x
    #             sim.set_seed()
    #             sim.set_seed(seed = x)
    #             sim.label = f"Sim {x} {j}"
    #             age_stats = cv.daily_age_stats(states = ['infectious'],edges = [12,18])
    #             analyzers = [age_stats]    
    #             sim.update_pars(analyzers=analyzers)
    #             sim.initialize()
    #             sim.run()
    #             agehist = sim.get_analyzer()
    #             x1 = agehist.results    
    #             dates = [datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in x1.keys()]
    #             values_new =  pd.DataFrame(np.array([list(value.values())[0] for _, value in agehist.results.items()]))
    #             values_0 = pd.concat([values_0,values_new[:][[0]]],axis = 1)
    #         final_median = pd.concat([final_median,values_0.median(axis=1)], axis = 1)
    #         final_25 = pd.concat([final_25,values_0.quantile(0.25,axis=1)], axis = 1)
    #         final_75 = pd.concat([final_75,values_0.quantile(0.75,axis=1)], axis = 1)
    #         final_0 = pd.concat([final_0,values_0.quantile(0,axis=1)], axis = 1)
    #         final_100 = pd.concat([final_100,values_0.quantile(1,axis=1)], axis = 1)
                
            
            
            
    #     _adol = pd.concat([pd.Series(dates),final_0,final_25,final_median,final_75,final_100],axis=1)
            
    #     _adol.columns = ['Date','0%_low','50%_low','70%_low','90%_low','0%_25','50%_25','70%_25','90%_25','0%_med',
    #                          '50%_med','70%_med','90%_med','0%_75','50%_75',
    #                          '70%_75','90%_75','0%_high','50%_high','70%_high',
    #                          '90%_high']
        
        
    #     _adol.to_excel(f'_adol_{j2}.xlsx')
    #         # _1218.to_excel('_1218_analyzers_dead.xlsx')
    #         # _1830.to_excel('_1830_analyzers_dead.xlsx')
    #         # _3050.to_excel('_3050_analyzers_dead.xlsx')
    #         # _5070.to_excel('_5070_analyzers_dead.xlsx')
    #         # _70100.to_excel('_70100_analyzers_dead.xlsx')


   
    
# =============================================================================
# 
#     length1 = len(list(x1.items()))
#     list_temp = list(x1.items()[0])
#     date_temp = list_temp[0]
#     value_temp = list_temp[1]
#     value_temp2 = list(value_temp.items())
#     value_temp3 = value_temp2[0]
#     values1_temp = value_temp3[1]
#     date = []
#     date += [date_temp]
#     values1 = values1_temp
#     
#     for i in range(length1-1):
#         list_temp = list(x1.items()[i+1])
#         date_temp = list_temp[0]
#         value_temp = list_temp[1]
#         value_temp2 = list(value_temp.items())
#         value_temp3 = value_temp2[0]
#         values1_temp = value_temp3[1]
#         date += [date_temp]
#         values1 = np.column_stack((values1, values1_temp))
#     
#         
#     dates = []
#     for i in range(length1):
#         date_ = datetime.strptime(date[0], '%Y-%m-%d').date()
#         dates.append(date_)
#         
#     ages = [12,18]
#     dataframe1 = pd.DataFrame({'Date': np.array([dt.datetime(2020, 1, 20)+dt.timedelta(days=i)
#                                                     for i in range(length1)])})
#     
#     x2 = agehist2.results
#     length2 = len(list(x2.items()))
#     list_temp = list(x2.items()[0])
#     date_temp = list_temp[0]
#     value_temp = list_temp[1]
#     value_temp2 = list(value_temp.items())
#     value_temp3 = value_temp2[0]
#     values2_temp = value_temp3[1]
#     date = []
#     date += [date_temp]
#     values2 = values2_temp
#     
#     for i in range(length2-1):
#         list_temp = list(x2.items()[i+1])
#         date_temp = list_temp[0]
#         value_temp = list_temp[1]
#         value_temp2 = list(value_temp.items())
#         value_temp3 = value_temp2[0]
#         values2_temp = value_temp3[1]
#         date += [date_temp]
#         values2 = np.column_stack((values2, values2_temp))
#     
#         
#     dates = []
#     for i in range(length2):
#         date_ = datetime.strptime(date[0], '%Y-%m-%d').date()
#         dates.append(date_)
#         
#     ages = [12,18]
#     dataframe2 = pd.DataFrame({'Date': np.array([dt.datetime(2020, 1, 20)+dt.timedelta(days=i)
#                                                     for i in range(length2)])})
#     
#     
#     x3 = agehist3.results
#     length3 = len(list(x3.items()))
#     list_temp = list(x3.items()[0])
#     date_temp = list_temp[0]
#     value_temp = list_temp[1]
#     value_temp2 = list(value_temp.items())
#     value_temp3 = value_temp2[0]
#     values3_temp = value_temp3[1]
#     date = []
#     date += [date_temp]
#     values3 = values3_temp
#     
#     for i in range(length3-1):
#         list_temp = list(x3.items()[i+1])
#         date_temp = list_temp[0]
#         value_temp = list_temp[1]
#         value_temp2 = list(value_temp.items())
#         value_temp3 = value_temp2[0]
#         values3_temp = value_temp3[1]
#         date += [date_temp]
#         values3 = np.column_stack((values3, values3_temp))
#     
#         
#     dates = []
#     for i in range(length3):
#         date_ = datetime.strptime(date[0], '%Y-%m-%d').date()
#         dates.append(date_)
#         
#     ages = [12,18]
#     dataframe3 = pd.DataFrame({'Date': np.array([dt.datetime(2020, 1, 20)+dt.timedelta(days=i)
#                                                     for i in range(length3)])})
#     
#     
#     x4 = agehist4.results
#     length4 = len(list(x4.items()))
#     list_temp = list(x4.items()[0])
#     date_temp = list_temp[0]
#     value_temp = list_temp[1]
#     value_temp2 = list(value_temp.items())
#     value_temp3 = value_temp2[0]
#     values4_temp = value_temp3[1]
#     date = []
#     date += [date_temp]
#     values4 = values4_temp
#     
#     for i in range(length4-1):
#         list_temp = list(x4.items()[i+1])
#         date_temp = list_temp[0]
#         value_temp = list_temp[1]
#         value_temp2 = list(value_temp.items())
#         value_temp3 = value_temp2[0]
#         values4_temp = value_temp3[1]
#         date += [date_temp]
#         values4 = np.column_stack((values4, values4_temp))
#     
#         
#     dates = []
#     for i in range(length4):
#         date_ = datetime.strptime(date[0], '%Y-%m-%d').date()
#         dates.append(date_)
#         
#     ages = [12,18]
#     dataframe4 = pd.DataFrame({'Date': np.array([dt.datetime(2020, 1, 20)+dt.timedelta(days=i)
#                                                     for i in range(length4)])})
#     
#     
#     pl.plot(dataframe1.Date, values1[0])
#     pl.plot(dataframe2.Date, values2[0])
#     pl.plot(dataframe3.Date, values3[0])
#     pl.plot(dataframe4.Date, values4[0])
# =============================================================================
# =============================================================================
#     pl.xlim(18281,18281+length1)
#     ax = pl.gca()
#     ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
#     pl.xlabel('Date')
#     
#     pl.title('Daily New Infectious Adolescents')
#     sc.dateformatter(ax=pl.gca(), style='sciris', dateformat = '%b', start = start_day, end = end_day)
#     pl.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,5,9)))
#     pl.legend(['0%','50%','70%','90%'])
# =============================================================================
#     agehist = cv.age_histogram(sim=sim) # Alternate method
#     agehist.plot(dateformat='concise')
# =============================================================================
    
# =============================================================================
#     msim.plot(to_plot = cumulative_ICUs, do_show = 1)
#     msim.plot(to_plot = cumulative_deaths)
#     msim.plot(to_plot = cumulative_hospitalisations)
#     msim.plot(to_plot = daily_infections_by_variant)
#     msim.plot(to_plot = daily_infectious)
#     msim.plot(to_plot = cumulative_infectious)
# =============================================================================

    


print('Done.')