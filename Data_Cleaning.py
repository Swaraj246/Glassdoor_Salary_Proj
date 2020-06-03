# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:16:56 2020

@author: Swaraj Panchal
"""

#loading the data into our workspace
import pandas as pd
df = pd.read_csv(('glassdoor_jobs.csv'))

################  CLEANING THE DATASET #############################

#----------------------- Cleaning the Salary Estimate Variable ---------------------------

#removing all the '-1' in the salary estimate

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate']!='-1']

Salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = Salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))

df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))

df['average_salary'] = (df.min_salary + df.max_salary)/2

#---------------------------- Clearing the ratings from the Company names ---------------------

df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#-------------------------- Cleaning the states variable ------------------------------

df['States'] = df['Location'].apply(lambda x: x.split(',')[1])
df['States'].value_counts()

df['Same State'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#------------------------- Calculating the age of the company from the year founded -----------------

df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2020 - x)

#-------------------------  finding important skills for the job ---------------------------------

df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

df['R_Studio'] = df['Job Description'].apply(lambda x: 1 if 'R-studio' in x.lower() or 'R studio' in x.lower() else 0)

df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'Tableau' in x.lower() else 0)

df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'Spark' in x.lower() else 0)

df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#----------------------- Dropping the first column since it is of no use -------------------------

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('Cleaned-Salary Data.csv', index = False)