#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:27:55 2024

@author: personal
"""

import pandas as pd
import pylab as pl
import sciris as sc 
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

pl.rcParams['lines.linewidth'] = 0.5

#df1 = pd.read_excel('Scenario_3.xlsx')
#df2 = pd.read_excel('Scenario_1.xlsx')
#df3 = pd.read_excel('Scenario_4.xlsx')
#df4 = pd.read_excel('Scenario_5.xlsx')

df1 = pd.read_excel('aa.xlsx')
df2 = pd.read_excel('af.xlsx')
df3 = pd.read_excel('ah.xlsx')
df4 = pd.read_excel('aj.xlsx')

pl.close('all')

pl.style.use('bmh')

start_day = '2021-09-01'
end_day = '2022-06-01'

#plot comparison of 0%, 50%, 70% and 90% of adolescents vaccinated

fig, ((ax1,ax2),(ax3, ax6),(ax4, ax5)) = pl.subplots(3,2,figsize = (20,20), dpi = 100)
fig.suptitle('Impact of Adolescent Vaccination on the Spread of Covid-19$^{*}$', y=0.98, fontsize = 18)
ax1.plot(df1.date, df1.new_infectious, color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax1.plot(df1.date, df1.new_infectious_low, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df1.date, df1.new_infectious_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df1.date, df1.new_infectious_low, df1.new_infectious_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax1.plot(df2.date, df2.new_infectious, color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax1.plot(df2.date, df2.new_infectious_low, color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df2.date, df2.new_infectious_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df2.date, df2.new_infectious_low, df2.new_infectious_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax1.plot(df3.date, df3.new_infectious, color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax1.plot(df3.date, df3.new_infectious_low, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df3.date, df3.new_infectious_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df3.date, df3.new_infectious_low, df3.new_infectious_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax1.plot(df4.date, df4.new_infectious, color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax1.plot(df4.date, df4.new_infectious_low, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.plot(df4.date, df4.new_infectious_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.fill_between(df4.date, df4.new_infectious_low, df4.new_infectious_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax1.set_title('Daily Number of Newly Infectious People')
sc.dateformatter(ax=ax1, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax1.legend(['No Adolescents Vaccinated', '50% Adolescents Vaccinated', '70% Adolescents Vaccinated', '90% Adolescents Vaccinated'], loc = 2, framealpha=0)
ax1.set_ylim([0, 860000])
ax1.tick_params(axis='x',)
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
#ax1.set_ylabel('Number of Infected People')



ax2.plot(df1.date, df1.cum_infectious, color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax2.plot(df1.date, df1.cum_infectious_low, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df1.date, df1.cum_infectious_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df1.date, df1.cum_infectious_low, df1.cum_infectious_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax2.plot(df2.date, df2.cum_infectious, color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax2.plot(df2.date, df2.cum_infectious_low, color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df2.date, df2.cum_infectious_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df2.date, df2.cum_infectious_low, df2.cum_infectious_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax2.plot(df3.date, df3.cum_infectious, color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax2.plot(df3.date, df3.cum_infectious_low, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df3.date, df3.cum_infectious_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df3.date, df3.cum_infectious_low, df3.cum_infectious_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax2.plot(df4.date, df4.cum_infectious, color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax2.plot(df4.date, df4.cum_infectious_low, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.plot(df4.date, df4.cum_infectious_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.fill_between(df4.date, df4.cum_infectious_low, df4.cum_infectious_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax2.set_title('Cumulative Number of Infectious People')
sc.dateformatter(ax=ax2, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax2.legend(['No Adolescents Vaccinated', '50% Adolescents Vaccinated', '70% Adolescents Vaccinated', '90% Adolescents Vaccinated'], loc = 2, framealpha=0)
ax2.set_ylim([15000000, 115000000])
ax2.tick_params(axis='x')
ax2.set_yticklabels(['{:,}'.format(int(x)) for x in ax2.get_yticks().tolist()])
#ax2.set_ylabel('Number of Infected People')

ax3.plot(df1.date, df1.r_eff, color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax3.plot(df1.date, df1.r_eff_low, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df1.date, df1.r_eff_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df1.date, df1.r_eff_low, df1.r_eff_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax3.plot(df2.date, df2.r_eff, color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax3.plot(df2.date, df2.r_eff_low, color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df2.date, df2.r_eff_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df2.date, df2.r_eff_low, df2.r_eff_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax3.plot(df3.date, df3.r_eff, color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax3.plot(df3.date, df3.r_eff_low, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df3.date, df3.r_eff_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df3.date, df3.r_eff_low, df3.r_eff_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax3.plot(df4.date, df4.r_eff, color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax3.plot(df4.date, df4.r_eff_low, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.plot(df4.date, df4.r_eff_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.fill_between(df4.date, df4.r_eff_low, df4.r_eff_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax3.set_title('Effective R Number')
sc.dateformatter(ax=ax3, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax3.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax3.legend(['No Adolescents Vaccinated', '50% Adolescents Vaccinated', '70% Adolescents Vaccinated', '90% Adolescents Vaccinated'], loc = 2, framealpha=0)
ax3.set_ylim([0.6,1.8])
ax3.tick_params(axis='x')
#ax3.set_yticklabels(['{:,}'.format(int(x)) for x in ax3.get_yticks().tolist()])
#ax3.set_ylabel('Number of Infected People')

ax4.plot(df1.date, df1.cum_severe, color = 'dodgerblue', alpha = 0.9, label = 'No Adolescents Vaccinated')
ax4.plot(df1.date, df1.cum_severe_low, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.plot(df1.date, df1.cum_severe_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df1.date, df1.cum_severe_low, df1.cum_severe_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax4.plot(df2.date, df2.cum_severe, color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax4.plot(df2.date, df2.cum_severe_low, color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.plot(df2.date, df2.cum_severe_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df2.date, df2.cum_severe_low, df2.cum_severe_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax4.plot(df3.date, df3.cum_severe, color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax4.plot(df3.date, df3.cum_severe_low, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.plot(df3.date, df3.cum_severe_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df3.date, df3.cum_severe_low, df3.cum_severe_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax4.plot(df4.date, df4.cum_severe, color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax4.plot(df4.date, df4.cum_severe_low, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax4.plot(df4.date, df4.cum_severe_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax4.fill_between(df4.date, df4.cum_severe_low, df4.cum_severe_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax4.set_title('Cumulative Number of Hospitalisations')
sc.dateformatter(ax=ax4, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax4.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax4.legend(['No Adolescents Vaccinated', '50% Adolescents Vaccinated', '70% Adolescents Vaccinated', '90% Adolescents Vaccinated'], loc = 2, framealpha=0)
ax4.set_ylim([350000,900000])
ax4.tick_params(axis='x')
ax4.set_yticklabels(['{:,}'.format(int(x)) for x in ax4.get_yticks().tolist()])
#ax4.set_ylabel('Number of Infected People')

ax5.plot(df1.date, df1.cum_deaths, color = 'dodgerblue', alpha = 0.9, label = '0% Adolescents Vaccinated')
ax5.plot(df1.date, df1.cum_deaths_low, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.plot(df1.date, df1.cum_deaths_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df1.date, df1.cum_deaths_low, df1.cum_deaths_high, color = 'dodgerblue', alpha = 0.1, label='_nolegend_')
ax5.plot(df2.date, df2.cum_deaths, color = 'orange', alpha = 0.9, label = '50% Adolescents Vaccinated')
ax5.plot(df2.date, df2.cum_deaths_low, color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.plot(df2.date, df2.cum_deaths_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df2.date, df2.cum_deaths_low, df2.cum_deaths_high, color = 'orange', alpha = 0.1, label='_nolegend_')
ax5.plot(df3.date, df3.cum_deaths, color = 'limegreen', alpha = 0.9, label = '70% Adolescents Vaccinated')
ax5.plot(df3.date, df3.cum_deaths_low, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.plot(df3.date, df3.cum_deaths_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df3.date, df3.cum_deaths_low, df3.cum_deaths_high, color = 'limegreen', alpha = 0.1, label='_nolegend_')
ax5.plot(df4.date, df4.cum_deaths, color = 'crimson', alpha = 0.9, label = '90% Adolescents Vaccinated')
ax5.plot(df4.date, df4.cum_deaths_low, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax5.plot(df4.date, df4.cum_deaths_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax5.fill_between(df4.date, df4.cum_deaths_low, df4.cum_deaths_high, color = 'crimson', alpha = 0.1, label='_nolegend_')
ax5.set_title('Cumulative Number of Deaths')
sc.dateformatter(ax=ax5, style='sciris', dateformat = '%b', start = start_day, end = end_day)
ax5.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(2,4,6,8,10,12)))
#ax5.legend(['No Adolescents Vaccinated', '50% Adolescents Vaccinated', '70% Adolescents Vaccinated', '90% Adolescents Vaccinated'], loc = 2, framealpha=0)
ax5.set_ylim([80000,190000])
ax5.tick_params(axis='x')
ax5.set_yticklabels(['{:,}'.format(int(x)) for x in ax5.get_yticks().tolist()])
#ax5.set_ylabel('Number of Infected People')

ax6.set_axis_off()
handles, labels = ax5.get_legend_handles_labels()
ax6.legend(handles, labels, loc = 'center')#, fontsize = 10,handlelength = 5, handleheight = 2.5)
ax6.set_title('$^{*}$modelling adolescent vaccination rollout from early August 2021', fontsize = 12, loc = 'center', y=0)
fig.tight_layout()

fig.savefig('Figure_7a.png', dpi = 300)



# plot bar chart comparison of 0%, 50%, 70% and 90% of adolescents vaccinated

fig, (ax7, ax8, ax9, ax10) = pl.subplots(4,1, figsize = (12,20), dpi = 40)
fig.suptitle('Impact of Adolescent Vaccination on the Spread of Covid-19$^{*}$', fontsize = 26, y=0.95)

l = list(df1.date)
sep21 = l.index(datetime(2021,9,1))
oct21 = l.index(datetime(2021,10,1))
nov21 = l.index(datetime(2021,11,1))
dec21 = l.index(datetime(2021,12,1))
jan22 = l.index(datetime(2022,1,1))
feb22 = l.index(datetime(2022,2,1))
mar22 = l.index(datetime(2022,3,1))
apr22 = l.index(datetime(2022,4,1))
may22 = l.index(datetime(2022,5,1))
jun22 = l.index(datetime(2022,6,1))
dates = [sep21, oct21,nov21,dec21,jan22,feb22,mar22,apr22,may22,jun22]

cum_infectious_list_1 = pd.array(df1.cum_infectious)
cum_infectious_list_2 = pd.array(df2.cum_infectious)
cum_infectious_list_3 = pd.array(df3.cum_infectious)
cum_infectious_list_4 = pd.array(df4.cum_infectious)

infectious_1 = np.empty(9,dtype=object)
infectious_2 = np.empty(9,dtype=object)
infectious_3 = np.empty(9,dtype=object)
infectious_4 = np.empty(9,dtype=object)

for i in range(9):
    infectious_1[i] = cum_infectious_list_1[dates[i+1]]-cum_infectious_list_1[dates[i]]#sum(cum_infectious_list_1[dates[i]:dates[i+1]])
    infectious_2[i] = cum_infectious_list_2[dates[i+1]]-cum_infectious_list_2[dates[i]]#sum(cum_infectious_list_2[dates[i]:dates[i+1]])
    infectious_3[i] = cum_infectious_list_3[dates[i+1]]-cum_infectious_list_3[dates[i]]
    infectious_4[i] = cum_infectious_list_4[dates[i+1]]-cum_infectious_list_4[dates[i]]
ind = np.arange(9) 
width = 1/5

date = ['Sep-21','Oct-21','Nov-21','Dec-21','Jan-22','Feb-22','Mar-22','Apr-22','May-22']


ax7.bar(ind+2/45, infectious_1, width, color = 'dodgerblue', label = '0% Adolescents Vaccinated')
ax7.bar(ind+11/45+1/45, infectious_2, width, color = 'orange', label = '50% Adolescents Vaccinated')
ax7.bar(ind+20/45+2/45, infectious_3, width, color = 'limegreen', label = '70% Adolescents Vaccinated')
ax7.bar(ind+29/45+3/45, infectious_4, width, color = 'crimson', label = '90% Adolescents Vaccinated')
ax7.set_xticks(ind+37/90, date)
#ax7.legend(framealpha=0)
ax7.set_xlim([-1/18,9-17/90])
ax7.set_xticks(ind+37/90, minor=True)
ax7.xaxis.set_tick_params(length = 0)
ax7.grid(which = 'minor')
ax7.grid(axis = 'x', which = 'major', alpha = 0)

#pl.ylim([-6900000,7900000])
#ax7.set_ylabel('Number of infectious')
ax7.set_ylim([0,21000000])
ax7.set_title('Total Number of Newly Infectious People Each Month', wrap = True)
ax7.set_yticklabels(['{:,}'.format(int(x)) for x in ax7.get_yticks().tolist()])




cum_severe_list_1 = pd.array(df1.cum_severe)
cum_severe_list_2 = pd.array(df2.cum_severe)
cum_severe_list_3 = pd.array(df3.cum_severe)
cum_severe_list_4 = pd.array(df4.cum_severe)

severe_1 = np.empty(9,dtype=object)
severe_2 = np.empty(9,dtype=object)
severe_3 = np.empty(9,dtype=object)
severe_4 = np.empty(9,dtype=object)

for i in range(9):
    severe_1[i] = cum_severe_list_1[dates[i+1]]-cum_severe_list_1[dates[i]]#sum(cum_severe_list_1[dates[i]:dates[i+1]])
    severe_2[i] = cum_severe_list_2[dates[i+1]]-cum_severe_list_2[dates[i]]#sum(cum_severe_list_2[dates[i]:dates[i+1]])
    severe_3[i] = cum_severe_list_3[dates[i+1]]-cum_severe_list_3[dates[i]]
    severe_4[i] = cum_severe_list_4[dates[i+1]]-cum_severe_list_4[dates[i]]
ind = np.arange(9) 
width = 1/5

date = ['Sep-21','Oct-21','Nov-21','Dec-21','Jan-22','Feb-22','Mar-22','Apr-22','May-22']


ax8.bar(ind+2/45, severe_1, width, color = 'dodgerblue', label = '0% Adolescents Vaccinated')
ax8.bar(ind+11/45+1/45, severe_2, width, color = 'orange', label = '50% Adolescents Vaccinated')
ax8.bar(ind+20/45+2/45, severe_3, width, color = 'limegreen', label = '70% Adolescents Vaccinated')
ax8.bar(ind+29/45+3/45, severe_4, width, color = 'crimson', label = '90% Adolescents Vaccinated')
ax8.set_xticks(ind+37/90, date)
#ax8.legend(framealpha=0)
ax8.set_xlim([-1/18,9-17/90])
ax8.set_xticks(ind+37/90, minor=True)
ax8.xaxis.set_tick_params(length = 0)
ax8.grid(which = 'minor')
ax8.grid(axis = 'x', which = 'major', alpha = 0)

#pl.ylim([-6900000,7900000])
#ax8.set_ylabel('Number of severe')
ax8.set_title('Total Number of Hospitalisations Each Month', wrap = True)
ax8.set_yticklabels(['{:,}'.format(int(x)) for x in ax8.get_yticks().tolist()])
ax8.set_ylim([0,80000])


cum_deaths_list_1 = pd.array(df1.cum_deaths)
cum_deaths_list_2 = pd.array(df2.cum_deaths)
cum_deaths_list_3 = pd.array(df3.cum_deaths)
cum_deaths_list_4 = pd.array(df4.cum_deaths)

deaths_1 = np.empty(9,dtype=object)
deaths_2 = np.empty(9,dtype=object)
deaths_3 = np.empty(9,dtype=object)
deaths_4 = np.empty(9,dtype=object)

for i in range(9):
    deaths_1[i] = cum_deaths_list_1[dates[i+1]]-cum_deaths_list_1[dates[i]]#sum(cum_deaths_list_1[dates[i]:dates[i+1]])
    deaths_2[i] = cum_deaths_list_2[dates[i+1]]-cum_deaths_list_2[dates[i]]#sum(cum_deaths_list_2[dates[i]:dates[i+1]])
    deaths_3[i] = cum_deaths_list_3[dates[i+1]]-cum_deaths_list_3[dates[i]]
    deaths_4[i] = cum_deaths_list_4[dates[i+1]]-cum_deaths_list_4[dates[i]]
ind = np.arange(9) 
width = 1/5

date = ['Sep-21','Oct-21','Nov-21','Dec-21','Jan-22','Feb-22','Mar-22','Apr-22','May-22']


ax9.bar(ind+2/45, deaths_1, width, color = 'dodgerblue', label = '0% Adolescents Vaccinated')
ax9.bar(ind+11/45+1/45, deaths_2, width, color = 'orange', label = '50% Adolescents Vaccinated')
ax9.bar(ind+20/45+2/45, deaths_3, width, color = 'limegreen', label = '70% Adolescents Vaccinated')
ax9.bar(ind+29/45+3/45, deaths_4, width, color = 'crimson', label = '90% Adolescents Vaccinated')
ax9.set_xticks(ind+37/90, date)
#ax9.legend(framealpha=0)
ax9.set_xlim([-1/18,9-17/90])
ax9.set_xticks(ind+37/90, minor=True)
ax9.xaxis.set_tick_params(length = 0)
ax9.grid(which = 'minor')
ax9.grid(axis = 'x', which = 'major', alpha = 0)

#pl.ylim([-6900000,7900000])
#ax9.set_ylabel('Number of deaths')
ax9.set_title('Total Number of Deaths Each Month', wrap = True)
ax9.set_yticklabels(['{:,}'.format(int(x)) for x in ax9.get_yticks().tolist()])
ax9.set_ylim([0,10000])


ax10.set_axis_off()
handles, labels = ax9.get_legend_handles_labels()
ax10.legend(handles, labels, loc = 'upper center')#, fontsize = 12,handlelength = 4, handleheight = 2)
ax10.set_title('$^{*}$modelling adolescent vaccination rollout from early August 2021', fontsize = 12, loc = 'center', y=0.6)

fig.savefig('Figure_7b.png', dpi = 300)