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

cv.check_version('>=3.1.4')
cv.git_info('covasim_version3.json')

#pl.close('all') #optional line

start_day = '2020-01-20'
end_day   = '2023-01-01'

def create_sim(x):

    start_day = '2020-01-20'
    end_day   = '2023-01-01'
    data_path = 'england_gov_data.xlsx'

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
        rel_severe_prob = 0.8,
        rel_crit_prob = 4.5,
    )

    sim = cv.Sim(pars=pars, datafile=data_path, end_day=end_day, location='uk')

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
                           '2021-09-07': [1.05, sbv_new, 0.30, 0.50],
                           '2021-09-15': [1.05, sbv_new, 0.30, 0.50],
                           '2021-09-29': [1.05, sbv_new, 0.30, 0.50],
                           '2021-10-15': [1.05, sbv_new, 0.30, 0.50],
                           #october half term
                           '2021-10-22': [1.05, 0.00, 0.30, 0.50],
                           '2021-10-29': [1.05, 0.00, 0.30, 0.50],
                           '2021-11-05': [1.05, sbv_new, 0.30, 0.50],
                           '2021-11-12': [1.05, sbv_new, 0.30, 0.50],
                           '2021-11-19': [1.05, sbv_new, 0.30, 0.50],
                           '2021-11-26': [1.05, sbv_new, 0.30, 0.50],
                           #mixing increases towards chrismas, especially within households and the community
                           '2021-12-01': [1.20, sbv_new, 0.30, 0.60],
                           '2021-12-09': [1.40, sbv_new, 0.40, 0.70],
                           '2021-12-16': [1.60, sbv_new, 0.40, 0.70],
                           #schools holidays
                           '2021-12-20': [2, 0.00, 0.40, 1.5],
                           '2021-12-31': [2, 0.00, 0.40, 1.5],
                           '2022-01-01': [2, 0.00, 0.40, 1.5],
                           #PlanB and schools open
                           
                           '2022-01-04': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-11': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-18': [1.0, sbv_new, 0.40, 0.60],
                           '2022-01-30': [1.0, sbv_new, 0.60, 0.60],
                           '2022-02-08': [1.0, sbv_new, 0.60, 0.60],
                           #february half term
                           '2022-02-15': [1.0, 0.00, 0.60, 0.70],
                           #school reopens
                           '2022-02-22': [1.0, 0.9, 0.70, 0.70],
                           #easter holidays
                           '2022-04-09': [1.0, 0.00, 0.80, 0.80],
                           #school reopens
                           '2022-04-22': [1.0, 0.9, 0.8, 0.8],
                           #may half term
                           '2022-05-28': [1.0, 0.00, 0.80, 0.90],
                           #school reopens
                           '2022-06-03': [1.0, 0.9, 0.80, 0.90],
                           #summer holidays
                           '2022-07-23': [1.0, 0.00, 0.8, 0.9],
                           #school reopens
                           '2022-08-31': [1.0, 0.9, 1, 1],
                           #october half term
                           '2022-10-22': [1.0, 0.00, 1, 1],
                           #school reopens
                           '2022-10-29': [1.0, 0.9, 1, 1],
                           #christmas holidays
                           '2022-12-19': [2.4, 0.00, 1, 2],
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
    b1177.p['rel_crit_prob']  = 15
    variants += [b1177]
    # Add Alpha strain to be present by October 2020
    b117 = cv.variant('Alpha', days=np.arange(sim.day('2020-10-20'), sim.day('2020-10-30')), n_imports=3000)
    b117.p['rel_beta']        = 1.8
    b117.p['rel_severe_prob'] = 0.7
    b117.p['rel_crit_prob']  = 18
    b117.p['rel_death_prob']  = 0.8
    variants += [b117]
    
    # Add Delta strain to be present by April 2021
    b16172 = cv.variant('Delta', days=np.arange(sim.day('2021-04-15'), sim.day('2021-04-20')), n_imports=4000)
    b16172.p['rel_beta']         = 2.6
    b16172.p['rel_severe_prob']  = 0.28
    b16172.p['rel_crit_prob']  = 7
    b16172.p['rel_death_prob']  = 0.35
    variants += [b16172]
    
    # Add Omicron BA.1 strain to be present by November 2021
    ba1 = cv.variant(label='omicron BA.1', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-10-16'), sim.day('2021-10-23')), n_imports=4000)
    ba1.p['rel_beta']         = 3.6
    ba1.p['rel_severe_prob']  = 0.19
    
    ba1.p['rel_death_prob']  = 0.4
    variants += [ba1]
    
    # Add Omicron BA.1.1 strain to be present by November 2021
    ba11 = cv.variant(label='omicron BA.1.1', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-10-23'), sim.day('2021-10-30')), n_imports=4000)    
    ba11.p['rel_beta']         = 3.1
    ba11.p['rel_severe_prob']  = 0.19
    ba11.p['rel_death_prob']  = 0.4
    variants += [ba11]
    
    # Add Omicron BA.2 strain to be present by January 2021
    ba2 = cv.variant(label='omicron BA.2', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2021-12-18'), sim.day('2021-12-25')), n_imports=4000)    
    ba2.p['rel_beta']         = 5.1
    ba2.p['rel_severe_prob']  = 0.23
    ba2.p['rel_death_prob']  = 0.4
    variants += [ba2]
    
    # Add Omicron BA.4 strain to be present by May 2021
    ba4 = cv.variant(label='omicron BA.4', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2022-03-19'), sim.day('2022-03-26')), n_imports=4000)    
    ba4.p['rel_beta']         = 5.0
    ba4.p['rel_severe_prob']  = 0.18
    ba4.p['rel_death_prob']  = 0.4
    variants += [ba4]
    
    # Add Omicron BA.5 strain to be present by May 2021
    ba5 = cv.variant(label='omicron BA.5', variant=cvp.get_variant_pars()['gamma'], days=np.arange(sim.day('2022-03-26'), sim.day('2022-04-02')), n_imports=4000)
    ba5.p['rel_beta']         = 5.5
    ba5.p['rel_severe_prob']  = 0.18
    ba5.p['rel_death_prob']  = 0.4
    variants += [ba5]
    
    sim['variants'] = variants
    sim.init_variants()
    sim.init_immunity()
    sim['immunity']
    
    #add variant cross immunities
    
    prior_b1177 = {'wild': 0.066, 'alpha': 0.500, 'beta': 1.000, 'gamma':0.040, 
                   'delta': 0.086, 'B.1.177': 1.000, 'omicron BA.1': 0.040, 'omicron BA.1.1': 0.040, 
                   'omicron BA.2': 0.040, 'omicron BA.4': 0.040, 'omicron BA.5': 0.040}
    
    prior_ba1 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.300, 
                 'delta': 0.03500, 'B.1.177': 0.050, 'omicron BA.1': 1.000,'omicron BA.1.1': 0.200, 
                 'omicron BA.2': 0.600, 'omicron BA.4': 0.100, 'omicron BA.5': 0.300}
    
    prior_ba11 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.300, 
                  'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.200, 'omicron BA.1.1': 1.000, 
                  'omicron BA.2': 0.600, 'omicron BA.4': 0.200, 'omicron BA.5': 0.200}
    
    prior_ba2 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.600, 'omicron BA.1.1': 0.600, 
                 'omicron BA.2': 1.000, 'omicron BA.4': 0.8, 'omicron BA.5': 0.6}
    
    prior_ba4 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.100, 'omicron BA.1.1': 0.100, 
                 'omicron BA.2': 0.8, 'omicron BA.4': 1.000, 'omicron BA.5': 0.500}
    
    prior_ba5 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.100, 'omicron BA.1.1': 0.100, 
                 'omicron BA.2': 0.6, 'omicron BA.4': 0.500, 'omicron BA.5': 1.000}
    
    pre_b1177 = {'wild': 0.066, 'alpha': 0.500, 'beta': 1.000, 'gamma':0.040, 
                   'delta': 0.086, 'B.1.177': 1.000, 'omicron BA.1': 0.040, 'omicron BA.1.1': 0.040, 
                   'omicron BA.2': 0.040, 'omicron BA.4': 0.040, 'omicron BA.5': 0.040}
    
    pre_ba1 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.300, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 1.000,'omicron BA.1.1': 0.200, 
                 'omicron BA.2': 0.600, 'omicron BA.4': 0.100, 'omicron BA.5': 0.300}
    
    pre_ba11 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.300, 
                  'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.200, 'omicron BA.1.1': 1.000, 
                  'omicron BA.2': 0.600, 'omicron BA.4': 0.200, 'omicron BA.5': 0.200}
    
    pre_ba2 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.600, 'omicron BA.1.1': 0.600, 
                 'omicron BA.2': 1.000, 'omicron BA.4': 0.8, 'omicron BA.5': 0.6}
    
    pre_ba4 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.300, 'omicron BA.1.1': 0.100, 
                 'omicron BA.2': 0.8, 'omicron BA.4': 1.000, 'omicron BA.5': 0.500}
    
    pre_ba5 = {'wild': 0.050, 'alpha': 0.050, 'beta': 0.040, 'gamma':0.100, 
                 'delta': 0.0350, 'B.1.177': 0.050, 'omicron BA.1': 0.300, 'omicron BA.1.1': 0.100, 
                 'omicron BA.2': 0.6, 'omicron BA.4': 0.500, 'omicron BA.5': 1.000}#0.5
    
    for k,v in sim['variant_map'].items():
        if v == 'B.1.177':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_b1177[j_lab]
                sim['immunity'][j][k] = pre_b1177[j_lab]
        if v == 'omicron BA.1':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba1[j_lab]
                sim['immunity'][j][k] = pre_ba1[j_lab]
        if v == 'omicron BA.1.1':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba11[j_lab]
                sim['immunity'][j][k] = pre_ba11[j_lab]
        if v == 'omicron BA.2':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba2[j_lab]
                sim['immunity'][j][k] = pre_ba2[j_lab]
        if v == 'omicron BA.4':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba4[j_lab]
                sim['immunity'][j][k] = pre_ba4[j_lab]
        if v == '0micron BA.5':
            for j, j_lab in sim['variant_map'].items():
                sim['immunity'][k][j] = prior_ba5[j_lab]
                sim['immunity'][j][k] = pre_ba5[j_lab]
        
    #define vaccine age groups, start day of vaccination and days to reach        
        
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
        16: dict(start_age=16, end_age=18, start_day='2021-08-04', days_to_reach=100),
        12: dict(start_age=12, end_age=16, start_day='2021-09-13', days_to_reach=121),
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
            vx_phase['daily_prob'] =0.0086
        elif (age>=12)*(age<16):
            vx_phase['daily_prob'] =0.0051
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
                           start_day='2022-04-01', end_day='2023-01-01',
                           quar_period=7),
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
    variant_pars = {'wild': 1.0, 'alpha': 1/2.3, 'beta': 1/9, 'gamma': 1/2.9, 
                    'delta': 1/6.2, 'B.1.177': 1/9, 'omicron BA.1': 1/2.9, 'omicron BA.1.1': 1/2.9, 
                    'omicron BA.2': 1/2.9, 'omicron BA.4': 1/2.9, 'omicron BA.5': 1/2.9}
    az_vaccine = sc.mergedicts({'label':'az_uk'}, sc.mergedicts(dose_pars, variant_pars)) 
    
    dose_pars = cvp.get_vaccine_dose_pars()['pfizer']
    dose_pars['interval'] = 7 * 8
    variant_pars = cvp.get_vaccine_variant_pars()['pfizer']
    variant_pars = {'wild': 1.0, 'alpha': 1/2.0, 'beta': 1/10.3, 'gamma': 1/6.7, 
                    'delta': 1/2.9, 'B.1.177': 1/10.3, 'omicron BA.1': 1/4.5, 'omicron BA.1.1': 1/4.5, 
                    'omicron BA.2': 1/4.5, 'omicron BA.4': 1/4.5, 'omicron BA.5': 1/4.5}
    pfizer_vaccine = sc.mergedicts({'label':'pfizer_uk'}, sc.mergedicts(dose_pars, variant_pars))
    
    # Slower dose roll out of Pfizer for those aged over 80 and aged below 18
    dose_pars = cvp.get_vaccine_dose_pars()['pfizer']
    dose_pars['interval'] = 7 * 12
    variant_pars = cvp.get_vaccine_variant_pars()['pfizer']
    variant_pars = {'wild': 1.0, 'alpha': 1/2.0, 'beta': 1/10.3, 'gamma': 1/6.7, 
                    'delta': 1/2.9, 'B.1.177': 1/10.3, 'omicron BA.1': 1/4.5, 'omicron BA.1.1': 1/4.5, 
                    'omicron BA.2': 1/4.5, 'omicron BA.4': 1/4.5, 'omicron BA.5': 1/4.5}
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
        beta=1/9.6,
        gamma=1/4.8,
        delta=1/4.5,)
    
    variantdict = {'omicron BA.1':1/3.7,
        'B.1.177':1/9.6,
        'omicron BA.1.1':1/3.7,
        'omicron BA.2':1/3.7,
        'omicron BA.4':1/3.7, 
        'omicron BA.5':1/3.7}
    
    booster = sc.mergedicts(dict1, variantdict)
    booster2 = sc.mergedicts(dict1, variantdict)
    booster3 = sc.mergedicts(dict1, variantdict)

    booster_target = {'inds': lambda sim: cv.true(sim.people.doses != 2),
                      'vals': 0}  # Only give boosters to people who have had 2 doses
    booster_target2 = {'inds': lambda sim: cv.true((sim.people.doses != 3)|(sim.people.age < 75)),
                      'vals': 0} # Only give Spring second booster to those aged over 75 who have already been boosted once
    booster_target3 = {'inds': lambda sim: cv.true((sim.people.doses != 3)|(sim.people.age < 50)|(sim.people.age>=75)),
                      'vals': 0} # Only give Spring second booster to those aged over 50 who have already been boosted once

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
     
        
    #prioritise by age 
    booster = cv.vaccinate_num(vaccine=booster, label='booster', sequence='age', subtarget=booster_target, num_doses=num_boosters, booster=True)
    booster2 = cv.vaccinate_num(vaccine=booster2, label='booster2', sequence='age', subtarget=booster_target2, num_doses=num_boosters2, booster=True)
    booster3 = cv.vaccinate_num(vaccine=booster3, label='booster3', sequence='age', subtarget=booster_target3, num_doses=num_boosters3, booster=True)
    interventions += [booster]
    interventions += [booster2]
    interventions += [booster3]

    # Finally, update the parameters
    sim.update_pars(interventions=interventions, variants=variants)
    for intervention in sim['interventions']:
        intervention.do_plot = False

    sim.initialize()
    return sim

if __name__ == '__main__':

    sim = create_sim([0])
    
    #loop over 100 times    
    sims = []
    for seed in range(30):
        sim = sim.copy()
        sim['rand_seed'] = seed
        sim.set_seed()
        sim.set_seed(seed=seed)
        sim.label = f"Sim {seed}"
        sims.append(sim)
        
    
    ###multisim running
    msim = cv.MultiSim(sims)
    msim.run(keep_people = 0)
    
    msim.reduce([0.05,0.95])
    
    
    
    daily_diagnoses = sc.objdict({
        'Baseline Scenario: Daily Number of Covid-19 Diagnoses': ['new_diagnoses']})
    
    cumulative_diagnoses = sc.objdict({
        'Baseline Scenario: Cumulative Number of Covid-19 Diagnoses': ['cum_diagnoses']})
    
    daily_infectious = sc.objdict({
        'Baseline Scenario: Daily Number of Infectious People': ['new_infectious']})
    
    daily_infections = sc.objdict({
        'Baseline Scenario: Daily Number of New Infections': ['new_infections']})
    
    new_tests = sc.objdict({
        'Baseline Scenario: Daily Number of Tests': ['new_tests']})
    
    daily_hospitalisations = sc.objdict({
        'Baseline Scenario: Daily Number of Hospitalisations due to Covid-19': ['new_severe']})
    
    daily_ICUs = sc.objdict({
        'Baseline Scenario: Daily umber of Hospitalisations (ICUs)': ['new_critical']})
    
    daily_deaths = sc.objdict({
        'Baseline Scenario: Daily Number of Fatalities due to Covid-19': ['new_deaths']})
    
    cumulative_hospitalisations = sc.objdict({
        'Baseline Scenario: Cumulative Number of Hospitalisations due to Covid-19': ['cum_severe']})
    
    cumulative_ICUs = sc.objdict({
        'Baseline Scenario: Cumulative Number of Hospitalisations (ICUs)': ['cum_critical']})
    
    cumulative_deaths = sc.objdict({
        'Baseline Scenario: Cumulative Number of Fatalities due to Covid-19': ['cum_deaths']})
    
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
    
    #saving the sims
    
    msim.to_excel('Scenario_1.xlsx')
    
    #plotting the sims
    
    
    # plot a figure of daily number of infectious people by variant from Sep 2020 to January 2022 - showing the emergence of Omicron
    
    msim.plot(to_plot = daily_infectious_by_variant, style='bmh', do_save = False, 
              fig_path = 'Figure_3.png', do_show = False, 
              tight = True, fig_args = {'num':'new_infectious_by_variant'}, 
              start = '2020-09-01', end = '2022-01-01', commaticks = True, 
              figsize = (10,4), dpi = 150)
    pl.gca().set_ylim([0, 400000])
    pl.savefig('Figure_3.png')
    
    #  plot a figure of daily number of infectious people by variant from Sep 2020 to January 2023 
    # add lines showing the dates of the simulated rollout of vaccines in adolescents (1st and 2nd dose).
    
    data = pd.read_excel('Scenario_1.xlsx')
    msim.plot(to_plot = daily_infectious_by_variant, style='bmh', do_save = False, do_show = False, 
              tight = True, fig_args = {'num':'new_infectious_by_variant'}, 
              start = '2020-09-01', end = end_day, 
              figsize = (10,4), dpi = 150, legend_args = {'loc': 'center right', 'bbox_to_anchor': (1.35, 0.5)})
    ax=pl.gca()
    ax.plot(data.date, data.new_infectious, color = 'black', alpha = 0.7, linewidth = 0.5)
    ax.axvline(x=data.date[563], color = 'black', linewidth=0.8)
    ax.axvline(x=data.date[647], color = 'black', linewidth=0.8)
    ax.axvline(x=data.date[604], color = 'black', linewidth=0.8)
    ax.axvline(x=data.date[688], color = 'black', linewidth=0.8)
    trans = ax.get_xaxis_transform()

    
    ax.text(data.date[550], .5, '1st vaccine for ages 16-17', transform = trans, rotation = 90, fontsize = 6)
    ax.text(data.date[591], .5, '1st vaccine for ages 12-15', transform = trans, rotation = 90, fontsize = 6)
    ax.text(data.date[634], .5, '2nd vaccine for ages 16-17', transform = trans, rotation = 90, fontsize = 6)
    ax.text(data.date[675], .5, '2nd vaccine for ages 12-15', transform = trans, rotation = 90, fontsize = 6)
    ax2=ax.twinx()
    ax2.set_ylim(0,3)
    ax2.grid(False)
    ax2.plot(data.date, data.r_eff, color='blue', alpha = 0.1, label = 'R number')
    ax2.plot(data.date, data.r_eff_low, color='blue', alpha = 0)
    ax2.plot(data.date, data.r_eff_high, color='blue', alpha = 0)
    ax2.fill_between(data.date, data.r_eff_low, data.r_eff_high, alpha = 0.1, color = 'blue')
    ax2.legend(framealpha = 0, loc = 'lower right', bbox_to_anchor = (1.2892, 0.117))
    pl.savefig('Figure_1.png')
    
    
print('Done.')
