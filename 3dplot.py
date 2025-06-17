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
import datetime as dt
import numpy as np
import time
import matplotlib.patches as mpatches


pl.rcParams['lines.linewidth'] = 0.5

aa = pd.read_excel('aa.xlsx')
ab = pd.read_excel('ab.xlsx')
ac = pd.read_excel('ac.xlsx')
ad = pd.read_excel('ad.xlsx')
ae = pd.read_excel('ae.xlsx')
af = pd.read_excel('af.xlsx')
ag = pd.read_excel('ag.xlsx')
ah = pd.read_excel('ah.xlsx')
ai = pd.read_excel('ai.xlsx')
aj = pd.read_excel('aj.xlsx')
ba = pd.read_excel('ba.xlsx')
bb = pd.read_excel('bb.xlsx')
bc = pd.read_excel('bc.xlsx')
bd = pd.read_excel('bd.xlsx')
be = pd.read_excel('be.xlsx')
bf = pd.read_excel('bf.xlsx')
bg = pd.read_excel('bg.xlsx')
bh = pd.read_excel('bh.xlsx')
bi = pd.read_excel('bi.xlsx')
bj = pd.read_excel('bj.xlsx')
ca = pd.read_excel('ca.xlsx')
cb = pd.read_excel('cb.xlsx')
cc = pd.read_excel('cc.xlsx')
cd = pd.read_excel('cd.xlsx')
ce = pd.read_excel('ce.xlsx')
cf = pd.read_excel('cf.xlsx')
cg = pd.read_excel('cg.xlsx')
ch = pd.read_excel('ch.xlsx')
ci = pd.read_excel('ci.xlsx')
cj = pd.read_excel('cj.xlsx')      
da = pd.read_excel('da.xlsx')
db = pd.read_excel('db.xlsx')
dc = pd.read_excel('dc.xlsx')
dd = pd.read_excel('dd.xlsx')
de = pd.read_excel('de.xlsx')
df = pd.read_excel('df.xlsx')
dg = pd.read_excel('dg.xlsx')
dh = pd.read_excel('dh.xlsx')
di = pd.read_excel('di.xlsx')
dj = pd.read_excel('dj.xlsx')
ea = pd.read_excel('ea.xlsx')
eb = pd.read_excel('eb.xlsx')
ec = pd.read_excel('ec.xlsx')
ed = pd.read_excel('ed.xlsx')
ee = pd.read_excel('ee.xlsx')
ef = pd.read_excel('ef.xlsx')
eg = pd.read_excel('eg.xlsx')
eh = pd.read_excel('eh.xlsx')
ei = pd.read_excel('ei.xlsx')
ej = pd.read_excel('ej.xlsx')
fa = pd.read_excel('fa.xlsx')
fb = pd.read_excel('fb.xlsx')
fc = pd.read_excel('fc.xlsx')
fd = pd.read_excel('fd.xlsx')
fe = pd.read_excel('fe.xlsx')
ff = pd.read_excel('ff.xlsx')
fg = pd.read_excel('fg.xlsx')
fh = pd.read_excel('fh.xlsx')
fi = pd.read_excel('fi.xlsx')
fj = pd.read_excel('fj.xlsx')

pl.close('all')

#pl.style.use('bmh')

start_day = '2021-09-01'
end_day = '2022-06-01'

x = list(range(0,10))
#y = ['week 0', 'week 2', 'week 4', 'week 6', 'week 8', 'week 10']
y = list(range(0,6))
i=743
#i=771
#i=802
z = [[aa.cum_infections[i], ab.cum_infections[i], ac.cum_infections[i], ad.cum_infections[i],ae.cum_infections[i],af.cum_infections[i],ag.cum_infections[i],ah.cum_infections[i],ai.cum_infections[i],aj.cum_infections[i]],
             [ba.cum_infections[i], bb.cum_infections[i], bc.cum_infections[i], bd.cum_infections[i],be.cum_infections[i],bf.cum_infections[i],bg.cum_infections[i],bh.cum_infections[i],bi.cum_infections[i],bj.cum_infections[i]],
             [ca.cum_infections[i], cb.cum_infections[i], cc.cum_infections[i], cd.cum_infections[i],ce.cum_infections[i],cf.cum_infections[i],cg.cum_infections[i],ch.cum_infections[i],ci.cum_infections[i],cj.cum_infections[i]],
             [da.cum_infections[i], db.cum_infections[i], dc.cum_infections[i], dd.cum_infections[i],de.cum_infections[i],df.cum_infections[i],dg.cum_infections[i],dh.cum_infections[i],di.cum_infections[i],dj.cum_infections[i]],
             [ea.cum_infections[i], eb.cum_infections[i], ec.cum_infections[i], ed.cum_infections[i],ee.cum_infections[i],ef.cum_infections[i],eg.cum_infections[i],eh.cum_infections[i],ei.cum_infections[i],ej.cum_infections[i]],
             [fa.cum_infections[i], fb.cum_infections[i], fc.cum_infections[i], fd.cum_infections[i],fe.cum_infections[i],ff.cum_infections[i],fg.cum_infections[i],fh.cum_infections[i],fi.cum_infections[i],fj.cum_infections[i]]]
             
z2 = [[element / 1000000 for element in sublist] for sublist in z]

fig = pl.figure(dpi = 100)
ax = fig.add_subplot(111, projection='3d')


ax.contourf(x,y,z2,300)


ax.tick_params(labelsize=8)    
pl.yticks(y, ['0','2','4','6','8','10'],fontsize = 8)
pl.xticks(x, ['0','10','20','30','40','50','60','70','80','90'],fontsize = 8)
pl.xlabel('% of adolescents vaccinated', fontsize = 8)
pl.ylabel('Vaccination delay (in weeks)', fontsize = 8)
ax.set_zlabel('Cumulative Number of infections (in millions)', fontsize = 8, rotation = 45)
pl.title('Cumulative Number of Infections on 01/03/22', fontsize = 10)
pl.savefig('01.03.22_3Dplot.png')

