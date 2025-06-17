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

england_data = pd.read_excel('england_infectious.xlsx')
england_infectious = pd.concat([england_data['date'],england_data['mid'],england_data['low'],england_data['high']],axis=1)

df0 = pd.read_excel('_adol_0.xlsx')
df1 = pd.read_excel('_adol_2.xlsx')
df2 = pd.read_excel('_adol_4.xlsx')
df = pd.concat([df0['Date'],df0['0%_25'],df0['0%_med'],df0['0%_75'],
                df0['50%_25'],df0['50%_med'],df0['50%_75'],
                df0['70%_25'],df0['70%_med'],df0['70%_75'],
                df0['90%_25'],df0['90%_med'],df0['90%_75']],axis=1)

df_1 = pd.concat([df1['Date'],df1['0%_25'],df1['0%_med'],df1['0%_75'],
                df1['50%_25'],df1['50%_med'],df1['50%_75'],
                df1['70%_25'],df1['70%_med'],df1['70%_75'],
                df1['90%_25'],df1['90%_med'],df1['90%_75']],axis=1)

df_2 = pd.concat([df2['Date'],df2['0%_25'],df2['0%_med'],df2['0%_75'],
                df2['50%_25'],df2['50%_med'],df2['50%_75'],
                df2['70%_25'],df2['70%_med'],df2['70%_75'],
                df2['90%_25'],df2['90%_med'],df2['90%_75']],axis=1)

start_day = '2021-08-01'
end_day = '2022-02-01'

pl.style.use('bmh')

fig, ((ax4,ax1),(ax5,ax2),(ax6,ax3)) = pl.subplots(3,2,figsize = (14,12), dpi = 100)
fig.suptitle('Impact of Adolescent Vaccination on the Daily Number of Infectious People', y=0.98, fontsize = 14)

ax1.plot(df.Date, df.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax1.plot(df.Date, df.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df.Date, df.iloc[:,1], df.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax1.plot(df.Date, df.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df.Date, df.iloc[:,4], df.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax1.plot(df.Date, df.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df.Date, df.iloc[:,7], df.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax1.plot(df.Date, df.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.plot(df.Date, df.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df.Date, df.iloc[:,10], df.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax1, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax1.set_ylim([0, 60000])
ax1.tick_params(axis='x')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()], fontsize = 8)
ax1.set_title('Daily Number of Infectious Adolescents: Adolescent Vaccination from August 2021', fontsize = 9)

ax2.plot(df_1.Date, df_1.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax2.plot(df_1.Date, df_1.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_1.Date, df_1.iloc[:,1], df_1.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax2.plot(df_1.Date, df_1.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_1.Date, df_1.iloc[:,4], df_1.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax2.plot(df_1.Date, df_1.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_1.Date, df_1.iloc[:,7], df_1.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax2.plot(df_1.Date, df_1.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.plot(df_1.Date, df_1.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df_1.Date, df_1.iloc[:,10], df_1.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax2, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax2.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax2.set_ylim([0, 60000])
ax2.tick_params(axis='x',)
ax2.set_yticklabels(['{:,}'.format(int(x)) for x in ax2.get_yticks().tolist()], fontsize = 8)
ax2.set_title('Daily Number of Infectious Adolescents: Adolescent Vaccination from September 2021', fontsize = 9)

ax3.plot(df_2.Date, df_2.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax3.plot(df_2.Date, df_2.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_2.Date, df_2.iloc[:,1], df_2.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax3.plot(df_2.Date, df_2.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_2.Date, df_2.iloc[:,4], df_2.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax3.plot(df_2.Date, df_2.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_2.Date, df_2.iloc[:,7], df_2.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax3.plot(df_2.Date, df_2.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.plot(df_2.Date, df_2.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df_2.Date, df_2.iloc[:,10], df_2.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax3, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax3.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax3.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax3.set_ylim([0, 60000])
ax3.tick_params(axis='x',)
ax3.set_yticklabels(['{:,}'.format(int(x)) for x in ax3.get_yticks().tolist()], fontsize = 8)
ax3.set_title('Daily Number of Infectious Adolescents: Adolescent Vaccination from October 2021', fontsize = 9)

ax1.axvline(df_2.Date[642], color = 'black', alpha = 0.6, linewidth = 0.5)
ax1.axvline(df_2.Date[655], color = 'black', alpha = 0.6, linewidth = 0.5)
ax2.axvline(df_2.Date[642], color = 'black', alpha = 0.6, linewidth = 0.5)
ax2.axvline(df_2.Date[655], color = 'black', alpha = 0.6, linewidth = 0.5)
ax3.axvline(df_2.Date[642], color = 'black', alpha = 0.6, linewidth = 0.5)
ax3.axvline(df_2.Date[655], color = 'black', alpha = 0.6, linewidth = 0.5)
trans1 = ax1.get_xaxis_transform()
trans2 = ax2.get_xaxis_transform()
trans3 = ax3.get_xaxis_transform()
ax1.text(df_2.Date[648], .5, 'October half term', transform = trans1, rotation = 90, fontsize = 6)
ax2.text(df_2.Date[648], .5, 'October half term', transform = trans2, rotation = 90, fontsize = 6)
ax3.text(df_2.Date[648], .5, 'October half term', transform = trans3, rotation = 90, fontsize = 6)


df3 = pd.read_excel('aa.xlsx')
df4 = pd.read_excel('af.xlsx')
df5 = pd.read_excel('ah.xlsx')
df6 = pd.read_excel('aj.xlsx')
df7 = pd.read_excel('ca.xlsx')
df8 = pd.read_excel('cf.xlsx')
df9 = pd.read_excel('ch.xlsx')
df10 = pd.read_excel('cj.xlsx')
df11 = pd.read_excel('ea.xlsx')
df12 = pd.read_excel('ef.xlsx')
df13 = pd.read_excel('eh.xlsx')
df14 = pd.read_excel('ej.xlsx')
df_3 = pd.concat([df3['date'],df3['new_infectious_low'],df3['new_infectious'],df3['new_infectious_high'],
                df4['new_infectious_low'],df4['new_infectious'],df4['new_infectious_high'],
                df5['new_infectious_low'],df5['new_infectious'],df5['new_infectious_high'],
                df6['new_infectious_low'],df6['new_infectious'],df6['new_infectious_high']],axis=1)

df_4 = pd.concat([df7['date'],df7['new_infectious_low'],df7['new_infectious'],df7['new_infectious_high'],
                df8['new_infectious_low'],df8['new_infectious'],df8['new_infectious_high'],
                df9['new_infectious_low'],df9['new_infectious'],df9['new_infectious_high'],
                df10['new_infectious_low'],df10['new_infectious'],df10['new_infectious_high']],axis=1)

df_5 = pd.concat([df11['date'],df11['new_infectious_low'],df11['new_infectious'],df11['new_infectious_high'],
                df12['new_infectious_low'],df12['new_infectious'],df12['new_infectious_high'],
                df13['new_infectious_low'],df13['new_infectious'],df13['new_infectious_high'],
                df14['new_infectious_low'],df14['new_infectious'],df14['new_infectious_high']],axis=1)

ax4.plot(df_3.date, df_3.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax4.plot(df_3.date, df_3.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df_3.date, df_3.iloc[:,1], df_3.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax4.plot(df_3.date, df_3.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df_3.date, df_3.iloc[:,4], df_3.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax4.plot(df_3.date, df_3.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df_3.date, df_3.iloc[:,7], df_3.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax4.plot(df_3.date, df_3.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax4.plot(df_3.date, df_3.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df_3.date, df_3.iloc[:,10], df_3.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax4, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax4.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax4.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax4.set_ylim([0, 800000])
ax4.tick_params(axis='x',)
ax4.set_yticklabels(['{:,}'.format(int(x)) for x in ax4.get_yticks().tolist()], fontsize = 8)
ax4.set_title('Daily Number of Infectious People: Adolescent Vaccination from August 2021', fontsize = 9)

ax5.plot(df_4.date, df_4.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax5.plot(df_4.date, df_4.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df_4.date, df_4.iloc[:,1], df_4.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax5.plot(df_4.date, df_4.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df_4.date, df_4.iloc[:,4], df_4.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax5.plot(df_4.date, df_4.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df_4.date, df_4.iloc[:,7], df_4.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax5.plot(df_4.date, df_4.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax5.plot(df_4.date, df_4.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df_4.date, df_4.iloc[:,10], df_4.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
#ax5.scatter(england_infectious.date,england_infectious.mid, marker='x', color = 'black')
#ax5.scatter(england_infectious.date,england_infectious.low, marker='x')
#ax5.scatter(england_infectious.date,england_infectious.high, marker='x')
sc.dateformatter(ax=ax5, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax5.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax5.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax5.set_ylim([0, 800000])
ax5.tick_params(axis='x',)
ax5.set_yticklabels(['{:,}'.format(int(x)) for x in ax5.get_yticks().tolist()], fontsize = 8)
ax5.set_title('Daily Number of Infectious People: Adolescent Vaccination from September 2021', fontsize = 9)

ax6.plot(df_5.date, df_5.iloc[:,2], color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax6.plot(df_5.date, df_5.iloc[:,1], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax6.fill_between(df_5.date, df_5.iloc[:,1], df_5.iloc[:,3], color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,5], color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax6.plot(df_5.date, df_5.iloc[:,4], color = 'orange', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax6.fill_between(df_5.date, df_5.iloc[:,4], df_5.iloc[:,6], color = 'orange', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,8], color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax6.plot(df_5.date, df_5.iloc[:,7], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax6.fill_between(df_5.date, df_5.iloc[:,7], df_5.iloc[:,9], color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,11], color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax6.plot(df_5.date, df_5.iloc[:,10], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax6.plot(df_5.date, df_5.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax6.fill_between(df_5.date, df_5.iloc[:,10], df_5.iloc[:,12], color = 'crimson', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax6, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax6.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax6.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)
ax6.set_ylim([0, 800000])
ax6.tick_params(axis='x',)
ax6.set_yticklabels(['{:,}'.format(int(x)) for x in ax6.get_yticks().tolist()], fontsize = 8)
ax6.set_title('Daily Number of Infectious People: Adolescent Vaccination from October 2021', fontsize = 9)
ax4.legend(['No Adolescents Vaccinated','50% Adolescents Vaccinated','70% Adolescents Vaccinated','90% Adolescents Vaccinated'], loc = 2, framealpha=0, fontsize = 8)

pl.tight_layout()


bs1 = pd.read_excel('booster_scenario3.xlsx')
bs2 = pd.read_excel('booster_scenario4.xlsx')


bs_1 = pd.concat([bs1['date'],bs1['new_infectious_low'],bs1['new_infectious'],bs1['new_infectious_high'],
                bs2['new_infectious_low'],bs2['new_infectious'],bs2['new_infectious_high']],axis=1)

bs = pd.read_excel('_1218_analyzers_2.xlsx')


start_day2 = '2022-08-01'
end_day2 = '2023-02-01'

pl.style.use('bmh')


fig, ((ax7,ax8)) = pl.subplots(1,2,figsize = (14,3.5), dpi = 100)
fig.suptitle('Impact of the Adolescent Booster Vaccine on the Number of Infectious People', y=0.98, fontsize = 12)


ax7.plot(bs_1.date, bs_1.iloc[:,2], color = 'crimson', alpha = 0.9)
ax7.plot(bs_1.date, bs_1.iloc[:,1], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax7.plot(bs_1.date, bs_1.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax7.fill_between(bs_1.date, bs_1.iloc[:,1], bs_1.iloc[:,3], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax7.plot(bs_1.date, bs_1.iloc[:,5], color = 'purple', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax7.plot(bs_1.date, bs_1.iloc[:,4], color = 'purple', alpha = 0.1, label='_nolegend_')
ax7.plot(bs_1.date, bs_1.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
ax7.fill_between(bs_1.date, bs_1.iloc[:,4], bs_1.iloc[:,6], color = 'purple', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax7, style='sciris', dateformat = '%b', start = start_day2, end = end_day2)
ax7.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax7.set_ylim([0, 350000])
#ax7.tick_params(axis='x',)
ax7.set_yticklabels(['{:,}'.format(int(x)) for x in ax7.get_yticks().tolist()], fontsize = 9)
ax7.set_title('Daily Number of Infectious People', fontsize = 8)


ax8.plot(bs.Date, bs['50+75+_Booster_med'], color = 'crimson', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax8.plot(bs.Date, bs['50+75+_Booster_25'], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.plot(bs.Date, bs['50+75+_Booster_75'], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.fill_between(bs.Date, bs['50+75+_Booster_25'], bs['50+75+_Booster_75'], color = 'crimson', alpha = 0.1, label='_nolegend_')
ax8.plot(bs.Date, bs['Adolescent_Booster_med'], color = 'purple', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax8.plot(bs.Date, bs['Adolescent_Booster_25'], color = 'purple', alpha = 0.1, label='_nolegend_')
ax8.plot(bs.Date, bs['Adolescent_Booster_75'], color = 'purple', alpha = 0.1, label='_nolegend_')
ax8.fill_between(bs.Date, bs['Adolescent_Booster_25'], bs['Adolescent_Booster_75'], color = 'purple', alpha = 0.1, label='_nolegend_')
sc.dateformatter(ax=ax8, style='sciris', dateformat = '%b', start = start_day2, end = end_day2)
ax8.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
ax8.set_ylim([0, 35000])
#ax8.tick_params(axis='x',)
ax8.set_yticklabels(['{:,}'.format(int(x)) for x in ax8.get_yticks().tolist()], fontsize = 9)
ax8.set_title('Daily Number of Infectious Adolescents', fontsize = 8)
ax8.legend(['Without Adolescent Booster', 'With Adolescent Booster'], loc = 2, framealpha=0, fontsize = 8)

pl.tight_layout()

###

bs1_ = pd.read_excel('booster_scenario3_.xlsx')
bs2_ = pd.read_excel('booster_scenario4_.xlsx')

sep2 = pd.read_excel('england_gov_data_trial.xlsx')


i = 744 #682, 713, 744, 


def bxplot(i):

    bs1_cum_inf = pd.array(bs1.cum_infections)
    bs1_cum_inf25 = pd.array(bs1.cum_infections_low)
    bs1_cum_inf75 = pd.array(bs1.cum_infections_high)
    bs1_cum_inf5 = pd.array(bs1_.cum_infections_low)
    bs1_cum_inf95 = pd.array(bs1_.cum_infections_high)

    bs1_median = bs1_cum_inf[i]
    bs1_q1 = bs1_cum_inf25[i]
    bs1_q3 = bs1_cum_inf75[i]
    bs1_min_val = bs1_cum_inf5[i]
    bs1_max_val = bs1_cum_inf95[i]
    
    bs2_cum_inf = pd.array(bs2.cum_infections)
    bs2_cum_inf25 = pd.array(bs2.cum_infections_low)
    bs2_cum_inf75 = pd.array(bs2.cum_infections_high)
    bs2_cum_inf5 = pd.array(bs2_.cum_infections_low)
    bs2_cum_inf95 = pd.array(bs2_.cum_infections_high)
    
    bs2_median = bs2_cum_inf[i]
    bs2_q1 = bs2_cum_inf25[i]
    bs2_q3 = bs2_cum_inf75[i]
    bs2_min_val = bs2_cum_inf5[i]
    bs2_max_val = bs2_cum_inf95[i]
    
    
        
    data = [np.concatenate([np.random.uniform(bs1_min_val, bs1_q1, 250), 
                            np.random.uniform(bs1_q1, bs1_median, 250), 
                            np.random.uniform(bs1_median, bs1_q3, 250), 
                            np.random.uniform(bs1_q3, bs1_max_val, 250)]),
            np.concatenate([np.random.uniform(bs2_min_val, bs2_q1, 250), 
                            np.random.uniform(bs2_q1, bs2_median, 250), 
                            np.random.uniform(bs2_median, bs2_q3, 250), 
                            np.random.uniform(bs2_q3, bs2_max_val, 250)])]
    
    return(data)

df1_ = pd.read_excel('af2.xlsx')
df2_ = pd.read_excel('ah2.xlsx')
df3_ = pd.read_excel('aj2.xlsx')
df4_ = pd.read_excel('cf2.xlsx')
df5_ = pd.read_excel('ch2.xlsx')
df6_ = pd.read_excel('cj2.xlsx')
df7_ = pd.read_excel('ef2.xlsx')
df8_ = pd.read_excel('eh2.xlsx')
df9_ = pd.read_excel('ej2.xlsx')
df0_ = pd.read_excel('aa2.xlsx')

def bxplot1(i):

    df1_cum_inf = pd.array(df4.cum_infections)
    df1_cum_inf25 = pd.array(df4.cum_infections_low)
    df1_cum_inf75 = pd.array(df4.cum_infections_high)
    df1_cum_inf5 = pd.array(df1_.cum_infections_low)
    df1_cum_inf95 = pd.array(df1_.cum_infections_high)

    df1_median = df1_cum_inf[i]
    df1_q1 = df1_cum_inf25[i]
    df1_q3 = df1_cum_inf75[i]
    df1_min_val = df1_cum_inf5[i]
    df1_max_val = df1_cum_inf95[i]
    
    df2_cum_inf = pd.array(df5.cum_infections)
    df2_cum_inf25 = pd.array(df5.cum_infections_low)
    df2_cum_inf75 = pd.array(df5.cum_infections_high)
    df2_cum_inf5 = pd.array(df2_.cum_infections_low)
    df2_cum_inf95 = pd.array(df2_.cum_infections_high)
    
    df2_median = df2_cum_inf[i]
    df2_q1 = df2_cum_inf25[i]
    df2_q3 = df2_cum_inf75[i]
    df2_min_val = df2_cum_inf5[i]
    df2_max_val = df2_cum_inf95[i]
    
    df3_cum_inf = pd.array(df6.cum_infections)
    df3_cum_inf25 = pd.array(df6.cum_infections_low)
    df3_cum_inf75 = pd.array(df6.cum_infections_high)
    df3_cum_inf5 = pd.array(df3_.cum_infections_low)
    df3_cum_inf95 = pd.array(df3_.cum_infections_high)
    
    df3_median = df3_cum_inf[i]
    df3_q1 = df3_cum_inf25[i]
    df3_q3 = df3_cum_inf75[i]
    df3_min_val = df3_cum_inf5[i]
    df3_max_val = df3_cum_inf95[i]
    
    df4_cum_inf = pd.array(df3.cum_infections)
    df4_cum_inf25 = pd.array(df3.cum_infections_low)
    df4_cum_inf75 = pd.array(df3.cum_infections_high)
    df4_cum_inf5 = pd.array(df0_.cum_infections_low)
    df4_cum_inf95 = pd.array(df0_.cum_infections_high)
    
    df4_median = df4_cum_inf[i]
    df4_q1 = df4_cum_inf25[i]
    df4_q3 = df4_cum_inf75[i]
    df4_min_val = df4_cum_inf5[i]
    df4_max_val = df4_cum_inf95[i]
    
    
        
    data = [np.concatenate([np.random.uniform(df4_min_val, df4_q1, 250), 
                            np.random.uniform(df4_q1, df4_median, 250), 
                            np.random.uniform(df4_median, df4_q3, 250), 
                            np.random.uniform(df4_q3, df4_max_val, 250)]),
            np.concatenate([np.random.uniform(df1_min_val, df1_q1, 250), 
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
                            np.random.uniform(df3_q3, df3_max_val, 250)])]
    
    return(data)



fig, axs = pl.subplots(1, 5, figsize=(15, 3.2))

sns.boxplot(data=bxplot(1016), ax = axs[0], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['crimson', 'purple'])
sns.boxplot(data=bxplot(1046), ax = axs[1], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['crimson', 'purple'])
sns.boxplot(data=bxplot(1077), ax = axs[2], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['crimson', 'purple'])
sns.boxplot(data=bxplot(1108), ax = axs[3], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['crimson', 'purple'])
sns.boxplot(data=bxplot(1136), ax = axs[4], linewidth = 0.8, width=0.5, showfliers = False, whis = 300, palette = ['crimson', 'purple'])

axs[0].set_ylabel('Cumulative Number of Infections', fontsize = 10)
axs[0].set_title('01/11/22')
axs[1].set_title('01/12/22')
axs[2].set_title('01/01/23')
axs[3].set_title('01/02/23')
axs[4].set_title('01/03/23')

axs[0].set_xticks([0,1])  
axs[0].set_xticklabels(['No BV', 'Adolescent BV']) 
#axs[0][0].set_xlabel('Adolescent Vaccine Uptake')
axs[0].set_ylim([125000000,134000000])
axs[1].set_ylim([130000000,140000000])
axs[2].set_ylim([136000000,147000000])
axs[3].set_ylim([140000000,154000000])
axs[4].set_ylim([143000000,158000000])

axs[1].set_xticks([0,1])  
axs[1].set_xticklabels(['No BV', 'Adolescent BV']) 
#axs[0][1].set_xlabel('Adolescent Vaccine Uptake')

axs[2].set_xticks([0,1])  
axs[2].set_xticklabels(['No BV', 'Adolescent BV']) 
#axs[0][2].set_xlabel('Adolescent Vaccine Uptake')

axs[3].set_xticks([0,1])  
axs[3].set_xticklabels(['No BV', 'Adolescent BV']) 
#axs[0][3].set_xlabel('Adolescent Vaccine Uptake')

axs[4].set_xticks([0,1])  
axs[4].set_xticklabels(['No BV', 'Adolescent BV']) 
#axs[0][4].set_xlabel('Adolescent Vaccine Uptake')

sep2_new = sep2.new_infectious
sep_cum_inf = pd.array(sep2_new.cumsum(axis=0))
sep_median1 = sep_cum_inf[1035]
sep_median2 = sep_cum_inf[1065]
sep_median3 = sep_cum_inf[1096]
sep_median4 = sep_cum_inf[1127]
sep_median5 = sep_cum_inf[1154]

axs[0].scatter(0,sep_median1, marker = 'x', color = 'black')
axs[1].scatter(0,sep_median2, marker = 'x', color = 'black')
axs[2].scatter(0,sep_median3, marker = 'x', color = 'black')
axs[3].scatter(0,sep_median4, marker = 'x', color = 'black')
axs[4].scatter(0,sep_median5, marker = 'x', color = 'black')
pl.tight_layout(pad = 3)
fig.suptitle('Cumulative Number of Infections')

fig.savefig('boxplot2_13may.png', dpi = 300)



