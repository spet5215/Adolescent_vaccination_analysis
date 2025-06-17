#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:36:13 2025

@author: personal
"""

import pandas as pd
import numpy as np
import pylab as pl
import sciris as sc
import covasim as cv
#import optuna as op
import covasim.parameters as cvp
#import covasim.immunity as cvi

from datetime import datetime
import datetime as dt
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib as plt

pl.close('all')


start_day = '2021-08-01'
end_day = '2022-02-01'

pl.style.use('bmh')

fig, ((ax1),(ax2),(ax3)) = pl.subplots(3,1,figsize = (8,12), dpi = 100)
fig.suptitle('Impact of Adolescent Vaccination on the Cumulative Number of Hospitalisations', y=0.98, fontsize = 12)



df3 = pd.read_excel('aa2.xlsx')
df4 = pd.read_excel('af2.xlsx')
df5 = pd.read_excel('ah2.xlsx')
df6 = pd.read_excel('aj2.xlsx')
df7 = pd.read_excel('ca2.xlsx')
df8 = pd.read_excel('cf2.xlsx')
df9 = pd.read_excel('ch2.xlsx')
df10 = pd.read_excel('cj2.xlsx')
df11 = pd.read_excel('ea2.xlsx')
df12 = pd.read_excel('ef2.xlsx')
df13 = pd.read_excel('eh2.xlsx')
df14 = pd.read_excel('ej2.xlsx')
df_3 = pd.concat([df3['date'],df3['new_severe_low'],df3['new_severe'],df3['new_severe_high'],
                df4['new_severe_low'],df4['new_severe'],df4['new_severe_high'],
                df5['new_severe_low'],df5['new_severe'],df5['new_severe_high'],
                df6['new_severe_low'],df6['new_severe'],df6['new_severe_high']],axis=1)

df_4 = pd.concat([df7['date'],df7['new_severe_low'],df7['new_severe'],df7['new_severe_high'],
                df8['new_severe_low'],df8['new_severe'],df8['new_severe_high'],
                df9['new_severe_low'],df9['new_severe'],df9['new_severe_high'],
                df10['new_severe_low'],df10['new_severe'],df10['new_severe_high']],axis=1)

df_5 = pd.concat([df11['date'],df11['new_severe_low'],df11['new_severe'],df11['new_severe_high'],
                df12['new_severe_low'],df12['new_severe'],df12['new_severe_high'],
                df13['new_severe_low'],df13['new_severe'],df13['new_severe_high'],
                df14['new_severe_low'],df14['new_severe'],df14['new_severe_high']],axis=1)

df_3_ = pd.concat([df3['date'],df3['cum_severe_low'],df3['cum_severe'],df3['cum_severe_high'],
                df4['cum_severe_low'],df4['cum_severe'],df4['cum_severe_high'],
                df5['cum_severe_low'],df5['cum_severe'],df5['cum_severe_high'],
                df6['cum_severe_low'],df6['cum_severe'],df6['cum_severe_high']],axis=1)

df_4_ = pd.concat([df7['date'],df7['cum_severe_low'],df7['cum_severe'],df7['cum_severe_high'],
                df8['cum_severe_low'],df8['cum_severe'],df8['cum_severe_high'],
                df9['cum_severe_low'],df9['cum_severe'],df9['cum_severe_high'],
                df10['cum_severe_low'],df10['cum_severe'],df10['cum_severe_high']],axis=1)

df_5_ = pd.concat([df11['date'],df11['cum_severe_low'],df11['cum_severe'],df11['cum_severe_high'],
                df12['cum_severe_low'],df12['cum_severe'],df12['cum_severe_high'],
                df13['cum_severe_low'],df13['cum_severe'],df13['cum_severe_high'],
                df14['cum_severe_low'],df14['cum_severe'],df14['cum_severe_high']],axis=1)




ax1.plot(df_3_.date, df_3_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,1], df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,4], df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,7], df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,10], df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax1, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax1.set_ylim([390000, 630000])
ax1.tick_params(axis='x',)
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()], fontsize = 8)
ax1.set_title('Adolescent Vaccination from August 2021', fontsize = 9)
ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)

ax2.plot(df_4_.date, df_4_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,1], df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,4], df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,7], df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,10], df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
#ax2.scatter(england_infectious.date,england_infectious.mid, marker='x', color = 'black')
#ax2.scatter(england_infectious.date,england_infectious.low, marker='x')
#ax2.scatter(england_infectious.date,england_infectious.high, marker='x')
sc.dateformatter(ax=ax2, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax2.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax2.set_ylim([390000, 630000])
ax2.tick_params(axis='x',)
ax2.set_yticklabels(['{:,}'.format(int(x)) for x in ax2.get_yticks().tolist()], fontsize = 8)
ax2.set_title('Adolescent Vaccination from September 2021', fontsize = 9)

ax3.plot(df_5_.date, df_5_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,1], df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,4], df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,7], df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,10], df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax3, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax3.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax3.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax3.set_ylim([390000, 630000])
ax3.tick_params(axis='x',)
ax3.set_yticklabels(['{:,}'.format(int(x)) for x in ax3.get_yticks().tolist()], fontsize = 8)
ax3.set_title('Adolescent Vaccination from October 2021', fontsize = 9)

pl.tight_layout()

pl.style.use('bmh')

fig, ((ax1),(ax2),(ax3)) = pl.subplots(3,1,figsize = (8,12), dpi = 100)
fig.suptitle('Impact of Adolescent Vaccination on the Cumulative Number of Hospitalisations (ICUs)', y=0.98, fontsize = 12)

df_3 = pd.concat([df3['date'],df3['new_critical_low'],df3['new_critical'],df3['new_critical_high'],
                df4['new_critical_low'],df4['new_critical'],df4['new_critical_high'],
                df5['new_critical_low'],df5['new_critical'],df5['new_critical_high'],
                df6['new_critical_low'],df6['new_critical'],df6['new_critical_high']],axis=1)

df_4 = pd.concat([df7['date'],df7['new_critical_low'],df7['new_critical'],df7['new_critical_high'],
                df8['new_critical_low'],df8['new_critical'],df8['new_critical_high'],
                df9['new_critical_low'],df9['new_critical'],df9['new_critical_high'],
                df10['new_critical_low'],df10['new_critical'],df10['new_critical_high']],axis=1)

df_5 = pd.concat([df11['date'],df11['new_critical_low'],df11['new_critical'],df11['new_critical_high'],
                df12['new_critical_low'],df12['new_critical'],df12['new_critical_high'],
                df13['new_critical_low'],df13['new_critical'],df13['new_critical_high'],
                df14['new_critical_low'],df14['new_critical'],df14['new_critical_high']],axis=1)

df_3_ = pd.concat([df3['date'],df3['cum_critical_low'],df3['cum_critical'],df3['cum_critical_high'],
                df4['cum_critical_low'],df4['cum_critical'],df4['cum_critical_high'],
                df5['cum_critical_low'],df5['cum_critical'],df5['cum_critical_high'],
                df6['cum_critical_low'],df6['cum_critical'],df6['cum_critical_high']],axis=1)

df_4_ = pd.concat([df7['date'],df7['cum_critical_low'],df7['cum_critical'],df7['cum_critical_high'],
                df8['cum_critical_low'],df8['cum_critical'],df8['cum_critical_high'],
                df9['cum_critical_low'],df9['cum_critical'],df9['cum_critical_high'],
                df10['cum_critical_low'],df10['cum_critical'],df10['cum_critical_high']],axis=1)

df_5_ = pd.concat([df11['date'],df11['cum_critical_low'],df11['cum_critical'],df11['cum_critical_high'],
                df12['cum_critical_low'],df12['cum_critical'],df12['cum_critical_high'],
                df13['cum_critical_low'],df13['cum_critical'],df13['cum_critical_high'],
                df14['cum_critical_low'],df14['cum_critical'],df14['cum_critical_high']],axis=1)

ax1.plot(df_3_.date, df_3_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,1], df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,4], df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,7], df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,10], df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax1, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax1.set_ylim([390000, 600000])
ax1.tick_params(axis='x',)
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()], fontsize = 8)
ax1.set_title('Adolescent Vaccination from August 2021', fontsize = 9)
ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)

ax2.plot(df_4_.date, df_4_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,1], df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,4], df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,7], df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,10], df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
#ax2.scatter(england_infectious.date,england_infectious.mid, marker='x', color = 'black')
#ax2.scatter(england_infectious.date,england_infectious.low, marker='x')
#ax2.scatter(england_infectious.date,england_infectious.high, marker='x')
sc.dateformatter(ax=ax2, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax2.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax2.set_ylim([390000, 600000])
ax2.tick_params(axis='x',)
ax2.set_yticklabels(['{:,}'.format(int(x)) for x in ax2.get_yticks().tolist()], fontsize = 8)
ax2.set_title('Adolescent Vaccination from September 2021', fontsize = 9)
              
ax3.plot(df_5_.date, df_5_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,1], df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,4], df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,7], df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,10], df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax3, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax3.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax3.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax3.set_ylim([390000, 600000])
ax3.tick_params(axis='x',)
ax3.set_yticklabels(['{:,}'.format(int(x)) for x in ax3.get_yticks().tolist()], fontsize = 8)
ax3.set_title('Adolescent Vaccination from October 2021', fontsize = 9)

pl.tight_layout()

pl.style.use('bmh')

fig, ((ax1),(ax2),(ax3)) = pl.subplots(3,1,figsize = (8,12), dpi = 100)
fig.suptitle('Impact of Adolescent Vaccination on the Cumulative Number of Deaths', y=0.98, fontsize = 12)

df_3 = pd.concat([df3['date'],df3['new_deaths_low'],df3['new_deaths'],df3['new_deaths_high'],
                df4['new_deaths_low'],df4['new_deaths'],df4['new_deaths_high'],
                df5['new_deaths_low'],df5['new_deaths'],df5['new_deaths_high'],
                df6['new_deaths_low'],df6['new_deaths'],df6['new_deaths_high']],axis=1)

df_4 = pd.concat([df7['date'],df7['new_deaths_low'],df7['new_deaths'],df7['new_deaths_high'],
                df8['new_deaths_low'],df8['new_deaths'],df8['new_deaths_high'],
                df9['new_deaths_low'],df9['new_deaths'],df9['new_deaths_high'],
                df10['new_deaths_low'],df10['new_deaths'],df10['new_deaths_high']],axis=1)

df_5 = pd.concat([df11['date'],df11['new_deaths_low'],df11['new_deaths'],df11['new_deaths_high'],
                df12['new_deaths_low'],df12['new_deaths'],df12['new_deaths_high'],
                df13['new_deaths_low'],df13['new_deaths'],df13['new_deaths_high'],
                df14['new_deaths_low'],df14['new_deaths'],df14['new_deaths_high']],axis=1)

df_3_ = pd.concat([df3['date'],df3['cum_deaths_low'],df3['cum_deaths'],df3['cum_deaths_high'],
                df4['cum_deaths_low'],df4['cum_deaths'],df4['cum_deaths_high'],
                df5['cum_deaths_low'],df5['cum_deaths'],df5['cum_deaths_high'],
                df6['cum_deaths_low'],df6['cum_deaths'],df6['cum_deaths_high']],axis=1)

df_4_ = pd.concat([df7['date'],df7['cum_deaths_low'],df7['cum_deaths'],df7['cum_deaths_high'],
                df8['cum_deaths_low'],df8['cum_deaths'],df8['cum_deaths_high'],
                df9['cum_deaths_low'],df9['cum_deaths'],df9['cum_deaths_high'],
                df10['cum_deaths_low'],df10['cum_deaths'],df10['cum_deaths_high']],axis=1)

df_5_ = pd.concat([df11['date'],df11['cum_deaths_low'],df11['cum_deaths'],df11['cum_deaths_high'],
                df12['cum_deaths_low'],df12['cum_deaths'],df12['cum_deaths_high'],
                df13['cum_deaths_low'],df13['cum_deaths'],df13['cum_deaths_high'],
                df14['cum_deaths_low'],df14['cum_deaths'],df14['cum_deaths_high']],axis=1)


ax1.plot(df_3_.date, df_3_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,1], df_3_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,4], df_3_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,7], df_3_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax1.plot(df_3_.date, df_3_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.plot(df_3_.date, df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df_3_.date, df_3_.iloc[:,10], df_3_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax1, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax1.set_ylim([100000, 150000])
ax1.tick_params(axis='x',)
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()], fontsize = 8)
ax1.set_title('Adolescent Vaccination from August 2021', fontsize = 9)
ax1.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)

ax2.plot(df_4_.date, df_4_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,1], df_4_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,4], df_4_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,7], df_4_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax2.plot(df_4_.date, df_4_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.plot(df_4_.date, df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_4_.date, df_4_.iloc[:,10], df_4_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
#ax2.scatter(england_infectious.date,england_infectious.mid, marker='x', color = 'black')
#ax2.scatter(england_infectious.date,england_infectious.low, marker='x')
#ax2.scatter(england_infectious.date,england_infectious.high, marker='x')
sc.dateformatter(ax=ax2, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax2.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax2.set_ylim([100000, 150000])
ax2.tick_params(axis='x',)
ax2.set_yticklabels(['{:,}'.format(int(x)) for x in ax2.get_yticks().tolist()], fontsize = 8)
ax2.set_title('Adolescent Vaccination from September 2021', fontsize = 9)
              
ax3.plot(df_5_.date, df_5_.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,1], df_5_.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,4], df_5_.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,7], df_5_.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax3.plot(df_5_.date, df_5_.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.plot(df_5_.date, df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_5_.date, df_5_.iloc[:,10], df_5_.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax3, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax3.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax3.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax3.set_ylim([100000, 150000])
ax3.tick_params(axis='x',)
ax3.set_yticklabels(['{:,}'.format(int(x)) for x in ax3.get_yticks().tolist()], fontsize = 8)
ax3.set_title('Adolescent Vaccination from October 2021', fontsize = 9)

pl.tight_layout()


bs1 = pd.read_excel('booster_scenario3.xlsx')
bs2 = pd.read_excel('booster_scenario4.xlsx')


bs_1 = pd.concat([bs1['date'],bs1['new_severe_low'],bs1['new_severe'],bs1['new_severe_high'],
                bs2['new_severe_low'],bs2['new_severe'],bs2['new_severe_high']],axis=1)

bs_1_ = pd.concat([bs1['date'],bs1['cum_severe_low'],bs1['cum_severe'],bs1['cum_severe_high'],
                bs2['cum_severe_low'],bs2['cum_severe'],bs2['cum_severe_high']],axis=1)


start_day2 = '2022-08-01'
end_day2 = '2023-02-01'

pl.style.use('bmh')

fig, ((ax8),(ax9),(ax10)) = pl.subplots(3,1,figsize = (8,12), dpi = 100)
fig.suptitle('Impact of the Adolescent Booster Vaccination on Hospitalisations and Deaths', y=0.98, fontsize = 12)



ax8.plot(bs_1_.date, bs_1_.iloc[:,2], color = 'crimson', alpha = 0.9)
ax8.plot(bs_1_.date, bs_1_.iloc[:,1], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.plot(bs_1_.date, bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.fill_between(bs_1_.date, bs_1_.iloc[:,1], bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.plot(bs_1_.date, bs_1_.iloc[:,5], color = 'purple', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax8.plot(bs_1_.date, bs_1_.iloc[:,4], color = 'purple', alpha = 0.1, label='_nolegend_')
ax8.plot(bs_1_.date, bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
ax8.fill_between(bs_1_.date, bs_1_.iloc[:,4], bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax8, style='sciris', dateformat = '%b', start = start_day2, end = end_day2)
ax8.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax8.set_ylim([750000, 1000000])
#ax7.tick_params(axis='x',)
ax8.set_yticklabels(['{:,}'.format(int(x)) for x in ax8.get_yticks().tolist()], fontsize = 9)
ax8.set_title('Cumulative Number of Hospitalisations', fontsize = 9)
ax8.legend(['Without Adolescent Booster', 'With Adolescent Booster'], loc = 2, framealpha=0, fontsize = 8)



bs_1 = pd.concat([bs1['date'],bs1['new_critical_low'],bs1['new_critical'],bs1['new_critical_high'],
                bs2['new_critical_low'],bs2['new_critical'],bs2['new_critical_high']],axis=1)

bs_1_ = pd.concat([bs1['date'],bs1['cum_critical_low'],bs1['cum_critical'],bs1['cum_critical_high'],
                bs2['cum_critical_low'],bs2['cum_critical'],bs2['cum_critical_high']],axis=1)



ax9.plot(bs_1_.date, bs_1_.iloc[:,2], color = 'crimson', alpha = 0.9)
ax9.plot(bs_1_.date, bs_1_.iloc[:,1], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax9.plot(bs_1_.date, bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax9.fill_between(bs_1_.date, bs_1_.iloc[:,1], bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax9.plot(bs_1_.date, bs_1_.iloc[:,5], color = 'purple', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax9.plot(bs_1_.date, bs_1_.iloc[:,4], color = 'purple', alpha = 0.1, label='_nolegend_')
ax9.plot(bs_1_.date, bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
ax9.fill_between(bs_1_.date, bs_1_.iloc[:,4], bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax9, style='sciris', dateformat = '%b', start = start_day2, end = end_day2)
ax9.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax9.set_ylim([610000, 720000])
#ax7.tick_params(axis='x',)
ax9.set_yticklabels(['{:,}'.format(int(x)) for x in ax9.get_yticks().tolist()], fontsize = 9)
ax9.set_title('Cumulative Number of Hospitalisations (ICUs)', fontsize = 9)
ax9.legend(['Without Adolescent Booster', 'With Adolescent Booster'], loc = 2, framealpha=0, fontsize = 8)



bs_1 = pd.concat([bs1['date'],bs1['new_deaths_low'],bs1['new_deaths'],bs1['new_deaths_high'],
                bs2['new_deaths_low'],bs2['new_deaths'],bs2['new_deaths_high']],axis=1)

bs_1_ = pd.concat([bs1['date'],bs1['cum_deaths_low'],bs1['cum_deaths'],bs1['cum_deaths_high'],
                bs2['cum_deaths_low'],bs2['cum_deaths'],bs2['cum_deaths_high']],axis=1)





ax10.plot(bs_1_.date, bs_1_.iloc[:,2], color = 'crimson', alpha = 0.9)
ax10.plot(bs_1_.date, bs_1_.iloc[:,1], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax10.plot(bs_1_.date, bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax10.fill_between(bs_1_.date, bs_1_.iloc[:,1], bs_1_.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax10.plot(bs_1_.date, bs_1_.iloc[:,5], color = 'purple', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax10.plot(bs_1_.date, bs_1_.iloc[:,4], color = 'purple', alpha = 0.1, label='_nolegend_')
ax10.plot(bs_1_.date, bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
ax10.fill_between(bs_1_.date, bs_1_.iloc[:,4], bs_1_.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax10, style='sciris', dateformat = '%b', start = start_day2, end = end_day2)
ax10.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax10.set_ylim([150000, 195000])
#ax7.tick_params(axis='x',)
ax10.set_yticklabels(['{:,}'.format(int(x)) for x in ax10.get_yticks().tolist()], fontsize = 9)
ax10.set_title('Cumulative Number of Deaths', fontsize = 9)
ax10.legend(['Without Adolescent Booster', 'With Adolescent Booster'], loc = 2, framealpha=0, fontsize = 8)

pl.tight_layout()


