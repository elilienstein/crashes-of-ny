#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:27:00 2019

@author: eric
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid")


# data = pd.read_csv('Motor_Vehicle_Crashes.csv', usecols=[9,13,14])
motor_vehicle_crashes_url = 'https://data.ny.gov/resource/xe9x-a24f.csv'
data = pd.read_csv(motor_vehicle_crashes_url, usecols=[9,13,14])

# column 9: State of Registration
# column 13: Contributing Factor 1 (HUMAN, ENVMT, VEHICLE)
# column 14: Contributing Factor 1 Description(Fell Asleep, Alcohol, Pavement Slippery...)

# Preprocessing the data

data.replace(["Not Applicable", "nan", "Unknown", "unknown" "Not Entered","Other*","Other"], np.nan, inplace=True)
data = data.dropna()
data['state_of_registration']=np.where(data['state_of_registration'] != 'NY', '0', data['state_of_registration'])
data['state_of_registration']=np.where(data['state_of_registration'] == 'NY', '1', data['state_of_registration'])

df = pd.crosstab(data.contributing_factor_1, data.state_of_registration)


df['Out'] = df['0']
df['In'] = df['1']
df = df.drop(['0', '1'], axis=1)
# data['%'] = data.apply(lambda row:row.In / row.Out, axis = 1)

print(df)
df.plot(kind='bar')

df2 = pd.crosstab(data.contributing_factor_1_description, data.state_of_registration)

df2['Out'] = df2['0']
df2['In'] = df2['1']
df2 = df2.drop(['0', '1'], axis=1)
df2['ratio'] = df2.apply(lambda row:row.Out / row.In, axis = 1)
print(df2)
