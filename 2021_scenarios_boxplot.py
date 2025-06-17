#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:55:19 2025

@author: personal
"""

import pandas as pd
import pylab as pl
import sciris as sc 
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pl.rcParams['lines.linewidth'] = 0.5

#df1 = pd.read_excel('Scenario_3.xlsx')
#df2 = pd.read_excel('Scenario_1.xlsx')
#df3 = pd.read_excel('Scenario_4.xlsx')
#df4 = pd.read_excel('Scenario_5.xlsx')

df1_ = pd.read_excel('aa2.xlsx')
df2_ = pd.read_excel('af2.xlsx')
df3_ = pd.read_excel('ah2.xlsx')
df4_ = pd.read_excel('aj2.xlsx')

df1 = pd.read_excel('aa.xlsx')
df2 = pd.read_excel('af.xlsx')
df3 = pd.read_excel('ah.xlsx')
df4 = pd.read_excel('aj.xlsx')

df5_ = pd.read_excel('ca2.xlsx')
df6_ = pd.read_excel('cf2.xlsx')
df7_ = pd.read_excel('ch2.xlsx')
df8_ = pd.read_excel('cj2.xlsx')

df5 = pd.read_excel('ca.xlsx')
df6 = pd.read_excel('cf.xlsx')
df7 = pd.read_excel('ch.xlsx')
df8 = pd.read_excel('cj.xlsx')

df9_ = pd.read_excel('ea2.xlsx')
df10_ = pd.read_excel('ef2.xlsx')
df11_ = pd.read_excel('eh2.xlsx')
df12_ = pd.read_excel('ej2.xlsx')

df9 = pd.read_excel('ea.xlsx')
df10 = pd.read_excel('ef.xlsx')
df11 = pd.read_excel('eh.xlsx')
df12 = pd.read_excel('ej.xlsx')

#sep = pd.read_excel('BASELINE2575.xlsx')
sep2 = pd.read_excel('england_gov_data_trial.xlsx')


i = 744 #682, 713, 744, 


def bxplot(i):

    df1_cum_inf = pd.array(df1.cum_infections)
    df1_cum_inf25 = pd.array(df1_.cum_infections_low)
    df1_cum_inf75 = pd.array(df1_.cum_infections_high)
    df1_cum_inf5 = pd.array(df1.cum_infections_low)
    df1_cum_inf95 = pd.array(df1.cum_infections_high)

    df1_median = df1_cum_inf[i]
    df1_q1 = df1_cum_inf25[i]
    df1_q3 = df1_cum_inf75[i]
    df1_min_val = df1_cum_inf5[i]
    df1_max_val = df1_cum_inf95[i]
    
    df2_cum_inf = pd.array(df2.cum_infections)
    df2_cum_inf25 = pd.array(df2_.cum_infections_low)
    df2_cum_inf75 = pd.array(df2_.cum_infections_high)
    df2_cum_inf5 = pd.array(df2.cum_infections_low)
    df2_cum_inf95 = pd.array(df2.cum_infections_high)
    
    df2_median = df2_cum_inf[i]
    df2_q1 = df2_cum_inf25[i]
    df2_q3 = df2_cum_inf75[i]
    df2_min_val = df2_cum_inf5[i]
    df2_max_val = df2_cum_inf95[i]
    
    df3_cum_inf = pd.array(df3.cum_infections)
    df3_cum_inf25 = pd.array(df3_.cum_infections_low)
    df3_cum_inf75 = pd.array(df3_.cum_infections_high)
    df3_cum_inf5 = pd.array(df3.cum_infections_low)
    df3_cum_inf95 = pd.array(df3.cum_infections_high)
    
    df3_median = df3_cum_inf[i]
    df3_q1 = df3_cum_inf25[i]
    df3_q3 = df3_cum_inf75[i]
    df3_min_val = df3_cum_inf5[i]
    df3_max_val = df3_cum_inf95[i]
    
    df4_cum_inf = pd.array(df4.cum_infections)
    df4_cum_inf25 = pd.array(df4_.cum_infections_low)
    df4_cum_inf75 = pd.array(df4_.cum_infections_high)
    df4_cum_inf5 = pd.array(df4.cum_infections_low)
    df4_cum_inf95 = pd.array(df4.cum_infections_high)
    
    df4_median = df4_cum_inf[i]
    df4_q1 = df4_cum_inf25[i]
    df4_q3 = df4_cum_inf75[i]
    df4_min_val = df4_cum_inf5[i]
    df4_max_val = df4_cum_inf95[i]
    
        
    data = [np.concatenate([np.random.uniform(df1_min_val, df1_q1, 250), 
                            np.random.uniform(df1_q1, df1_median, 250), 
                            np.random.uniform(df1_median, df1_q3, 250), 
                            np.random.uniform(df1_q3, df1_max_val, 250)]),
            np.concatenate([np.random.uniform(df2_min_val, df2_q1, 250), 
                            np.random.uniform(df2_q1, df2_median, 250), 
                            np.random.uniform(df2_median, df2_q3, 250), 
                            np.random.uniform(df2_q3, df2_max_val, 250)]),
            np.concatenate([np.random.uniform(df3_min_val, df3_q1, 250), 
                            np.random.uniform(df3_q1, df3_median, 250), 
                            np.random.uniform(df3_median, df3_q3, 250), 
                            np.random.uniform(df3_q3, df3_max_val, 250)]),
            np.concatenate([np.random.uniform(df4_min_val, df4_q1, 250), 
                            np.random.uniform(df4_q1, df4_median, 250), 
                            np.random.uniform(df4_median, df4_q3, 250), 
                            np.random.uniform(df4_q3, df4_max_val, 250)])]
    
    return(data)

def bxplot1(i):

    df5_cum_inf = pd.array(df5.cum_infections)
    df5_cum_inf25 = pd.array(df5_.cum_infections_low)
    df5_cum_inf75 = pd.array(df5_.cum_infections_high)
    df5_cum_inf5 = pd.array(df5.cum_infections_low)
    df5_cum_inf95 = pd.array(df5.cum_infections_high)

    df5_median = df5_cum_inf[i]
    df5_q1 = df5_cum_inf25[i]
    df5_q3 = df5_cum_inf75[i]
    df5_min_val = df5_cum_inf5[i]
    df5_max_val = df5_cum_inf95[i]
    
    df6_cum_inf = pd.array(df6.cum_infections)
    df6_cum_inf25 = pd.array(df6_.cum_infections_low)
    df6_cum_inf75 = pd.array(df6_.cum_infections_high)
    df6_cum_inf5 = pd.array(df6.cum_infections_low)
    df6_cum_inf95 = pd.array(df6.cum_infections_high)
    
    df6_median = df6_cum_inf[i]
    df6_q1 = df6_cum_inf25[i]
    df6_q3 = df6_cum_inf75[i]
    df6_min_val = df6_cum_inf5[i]
    df6_max_val = df6_cum_inf95[i]
    
    df7_cum_inf = pd.array(df7.cum_infections)
    df7_cum_inf25 = pd.array(df7_.cum_infections_low)
    df7_cum_inf75 = pd.array(df7_.cum_infections_high)
    df7_cum_inf5 = pd.array(df7.cum_infections_low)
    df7_cum_inf95 = pd.array(df7.cum_infections_high)
    
    df7_median = df7_cum_inf[i]
    df7_q1 = df7_cum_inf25[i]
    df7_q3 = df7_cum_inf75[i]
    df7_min_val = df7_cum_inf5[i]
    df7_max_val = df7_cum_inf95[i]
    
    df8_cum_inf = pd.array(df8.cum_infections)
    df8_cum_inf25 = pd.array(df8_.cum_infections_low)
    df8_cum_inf75 = pd.array(df8_.cum_infections_high)
    df8_cum_inf5 = pd.array(df8.cum_infections_low)
    df8_cum_inf95 = pd.array(df8.cum_infections_high)
    
    df8_median = df8_cum_inf[i]
    df8_q1 = df8_cum_inf25[i]
    df8_q3 = df8_cum_inf75[i]
    df8_min_val = df8_cum_inf5[i]
    df8_max_val = df8_cum_inf95[i]
    
        
    data = [np.concatenate([np.random.uniform(df5_min_val, df5_q1, 250), 
                            np.random.uniform(df5_q1, df5_median, 250), 
                            np.random.uniform(df5_median, df5_q3, 250), 
                            np.random.uniform(df5_q3, df5_max_val, 250)]),
            np.concatenate([np.random.uniform(df6_min_val, df6_q1, 250), 
                            np.random.uniform(df6_q1, df6_median, 250), 
                            np.random.uniform(df6_median, df6_q3, 250), 
                            np.random.uniform(df6_q3, df6_max_val, 250)]),
            np.concatenate([np.random.uniform(df7_min_val, df7_q1, 250), 
                            np.random.uniform(df7_q1, df7_median, 250), 
                            np.random.uniform(df7_median, df7_q3, 250), 
                            np.random.uniform(df7_q3, df7_max_val, 250)]),
            np.concatenate([np.random.uniform(df8_min_val, df8_q1, 250), 
                            np.random.uniform(df8_q1, df8_median, 250), 
                            np.random.uniform(df8_median, df8_q3, 250), 
                            np.random.uniform(df8_q3, df8_max_val, 250)])]
    
    return(data)

def bxplot2(i):

    df9_cum_inf = pd.array(df9.cum_infections)
    df9_cum_inf25 = pd.array(df9_.cum_infections_low)
    df9_cum_inf75 = pd.array(df9_.cum_infections_high)
    df9_cum_inf5 = pd.array(df9.cum_infections_low)
    df9_cum_inf95 = pd.array(df9.cum_infections_high)

    df9_median = df9_cum_inf[i]
    df9_q1 = df9_cum_inf25[i]
    df9_q3 = df9_cum_inf75[i]
    df9_min_val = df9_cum_inf5[i]
    df9_max_val = df9_cum_inf95[i]
    
    df10_cum_inf = pd.array(df10.cum_infections)
    df10_cum_inf25 = pd.array(df10_.cum_infections_low)
    df10_cum_inf75 = pd.array(df10_.cum_infections_high)
    df10_cum_inf5 = pd.array(df10.cum_infections_low)
    df10_cum_inf95 = pd.array(df10.cum_infections_high)
    
    df10_median = df10_cum_inf[i]
    df10_q1 = df10_cum_inf25[i]
    df10_q3 = df10_cum_inf75[i]
    df10_min_val = df10_cum_inf5[i]
    df10_max_val = df10_cum_inf95[i]
    
    df11_cum_inf = pd.array(df11.cum_infections)
    df11_cum_inf25 = pd.array(df11_.cum_infections_low)
    df11_cum_inf75 = pd.array(df11_.cum_infections_high)
    df11_cum_inf5 = pd.array(df11.cum_infections_low)
    df11_cum_inf95 = pd.array(df11.cum_infections_high)
    
    df11_median = df11_cum_inf[i]
    df11_q1 = df11_cum_inf25[i]
    df11_q3 = df11_cum_inf75[i]
    df11_min_val = df11_cum_inf5[i]
    df11_max_val = df11_cum_inf95[i]
    
    df12_cum_inf = pd.array(df12.cum_infections)
    df12_cum_inf25 = pd.array(df12_.cum_infections_low)
    df12_cum_inf75 = pd.array(df12_.cum_infections_high)
    df12_cum_inf5 = pd.array(df12.cum_infections_low)
    df12_cum_inf95 = pd.array(df12.cum_infections_high)
    
    df12_median = df12_cum_inf[i]
    df12_q1 = df12_cum_inf25[i]
    df12_q3 = df12_cum_inf75[i]
    df12_min_val = df12_cum_inf5[i]
    df12_max_val = df12_cum_inf95[i]
    
        
    data = [np.concatenate([np.random.uniform(df9_min_val, df9_q1, 250), 
                            np.random.uniform(df9_q1, df9_median, 250), 
                            np.random.uniform(df9_median, df9_q3, 250), 
                            np.random.uniform(df9_q3, df9_max_val, 250)]),
            np.concatenate([np.random.uniform(df10_min_val, df10_q1, 250), 
                            np.random.uniform(df10_q1, df10_median, 250), 
                            np.random.uniform(df10_median, df10_q3, 250), 
                            np.random.uniform(df10_q3, df10_max_val, 250)]),
            np.concatenate([np.random.uniform(df11_min_val, df11_q1, 250), 
                            np.random.uniform(df11_q1, df11_median, 250), 
                            np.random.uniform(df11_median, df11_q3, 250), 
                            np.random.uniform(df11_q3, df11_max_val, 250)]),
            np.concatenate([np.random.uniform(df12_min_val, df12_q1, 250), 
                            np.random.uniform(df12_q1, df12_median, 250), 
                            np.random.uniform(df12_median, df12_q3, 250), 
                            np.random.uniform(df12_q3, df12_max_val, 250)])]
    
    return(data)
pl.style.use('bmh')

fig, axs = plt.subplots(3, 5, figsize=(15, 15))

sns.boxplot(data=bxplot(681), ax = axs[0][0], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot(712), ax = axs[0][1], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot(743), ax = axs[0][2], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot(771), ax = axs[0][3], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot(802), ax = axs[0][4], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])

axs[0][0].set_ylabel('Vaccine rollout August 2021', fontsize = 10)
axs[0][0].set_title('01/12/21')
axs[0][1].set_title('01/01/22')
axs[0][2].set_title('01/02/22')
axs[0][3].set_title('01/03/22')
axs[0][4].set_title('01/04/22')

axs[0][0].set_xticks([0,1,2,3])  
axs[0][0].set_xticklabels(['0%','50%','70%','90%']) 
#axs[0][0].set_xlabel('Adolescent Vaccine Uptake')
axs[0][0].set_ylim([27000000,39000000])
axs[1][0].set_ylim([27000000,39000000])
axs[2][0].set_ylim([27000000,39000000])
axs[0][1].set_ylim([33000000,49000000])
axs[0][2].set_ylim([41000000,61000000])
axs[0][3].set_ylim([55000000,71000000])
axs[0][4].set_ylim([68000000,87000000])
axs[1][1].set_ylim([33000000,49000000])
axs[1][2].set_ylim([41000000,61000000])
axs[1][3].set_ylim([55000000,71000000])
axs[1][4].set_ylim([68000000,87000000])
axs[2][1].set_ylim([33000000,49000000])
axs[2][2].set_ylim([41000000,61000000])
axs[2][3].set_ylim([55000000,71000000])
axs[2][4].set_ylim([68000000,87000000])

axs[0][1].set_xticks([0,1,2,3])  
axs[0][1].set_xticklabels(['0%','50%','70%','90%']) 
#axs[0][1].set_xlabel('Adolescent Vaccine Uptake')

axs[0][2].set_xticks([0,1,2,3])  
axs[0][2].set_xticklabels(['0%','50%','70%','90%']) 
#axs[0][2].set_xlabel('Adolescent Vaccine Uptake')

axs[0][3].set_xticks([0,1,2,3])  
axs[0][3].set_xticklabels(['0%','50%','70%','90%']) 
#axs[0][3].set_xlabel('Adolescent Vaccine Uptake')

axs[0][4].set_xticks([0,1,2,3])  
axs[0][4].set_xticklabels(['0%','50%','70%','90%']) 
#axs[0][4].set_xlabel('Adolescent Vaccine Uptake')

sns.boxplot(data=bxplot1(681), ax = axs[1][0], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot1(712), ax = axs[1][1], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot1(743), ax = axs[1][2], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot1(771), ax = axs[1][3], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot1(802), ax = axs[1][4], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])

axs[1][0].set_ylabel('Vaccine rollout September 2021', fontsize = 10)


axs[1][0].set_xticks([0,1,2,3])  
axs[1][0].set_xticklabels(['0%','50%','70%','90%']) 
#axs[1][0].set_xlabel('Adolescent Vaccine Uptake')

axs[1][1].set_xticks([0,1,2,3])  
axs[1][1].set_xticklabels(['0%','50%','70%','90%']) 
#axs[1][1].set_xlabel('Adolescent Vaccine Uptake')

axs[1][2].set_xticks([0,1,2,3])  
axs[1][2].set_xticklabels(['0%','50%','70%','90%']) 
#axs[1][2].set_xlabel('Adolescent Vaccine Uptake')

axs[1][3].set_xticks([0,1,2,3])  
axs[1][3].set_xticklabels(['0%','50%','70%','90%']) 
#axs[1][3].set_xlabel('Adolescent Vaccine Uptake')

axs[1][4].set_xticks([0,1,2,3])  
axs[1][4].set_xticklabels(['0%','50%','70%','90%']) 
#axs[1][4].set_xlabel('Adolescent Vaccine Uptake')

sns.boxplot(data=bxplot2(681), ax = axs[2][0], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot2(712), ax = axs[2][1], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot2(743), ax = axs[2][2], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot2(771), ax = axs[2][3], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])
sns.boxplot(data=bxplot2(802), ax = axs[2][4], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['dodgerblue', 'orange', 'limegreen', 'crimson'])

sep2_new = sep2.new_infectious
sep_cum_inf = pd.array(sep2_new.cumsum(axis=0))
sep_median1 = sep_cum_inf[700]
sep_median2 = sep_cum_inf[731]
sep_median3 = sep_cum_inf[762]
sep_median4 = sep_cum_inf[790]
sep_median5 = sep_cum_inf[821]

axs[1][0].scatter(1,sep_median1, marker = 'x', color = 'black')
axs[1][1].scatter(1,sep_median2, marker = 'x', color = 'black')
axs[1][2].scatter(1,sep_median3, marker = 'x', color = 'black')
axs[1][3].scatter(1,sep_median4, marker = 'x', color = 'black')
axs[1][4].scatter(1,sep_median5, marker = 'x', color = 'black')

axs[2][0].set_ylabel('Vaccine rollout October 2021', fontsize = 10)


axs[2][0].set_xticks([0,1,2,3])  
axs[2][0].set_xticklabels(['0%','50%','70%','90%']) 
axs[2][0].set_xlabel('Adolescent Vaccine Uptake')

axs[2][1].set_xticks([0,1,2,3])  
axs[2][1].set_xticklabels(['0%','50%','70%','90%']) 
axs[2][1].set_xlabel('Adolescent Vaccine Uptake')

axs[2][2].set_xticks([0,1,2,3])  
axs[2][2].set_xticklabels(['0%','50%','70%','90%']) 
axs[2][2].set_xlabel('Adolescent Vaccine Uptake')

axs[2][3].set_xticks([0,1,2,3])  
axs[2][3].set_xticklabels(['0%','50%','70%','90%']) 
axs[2][3].set_xlabel('Adolescent Vaccine Uptake')

axs[2][4].set_xticks([0,1,2,3])  
axs[2][4].set_xticklabels(['0%','50%','70%','90%']) 
axs[2][4].set_xlabel('Adolescent Vaccine Uptake')

plt.tight_layout(pad = 3)

fig.suptitle('Cumulative Number of Infections')

#fig.savefig('boxplot1_13may.png', dpi = 300)