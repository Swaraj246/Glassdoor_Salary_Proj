# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:13:15 2020

@author: Swaraj Panchal
"""
import glassdoor_scrapper as gs
import pandas as pd
path = "C:/Users/13129/Documents/Glassdoor_Salary_Proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv',index = False)