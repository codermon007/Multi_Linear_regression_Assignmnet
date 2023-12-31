# -*- coding: utf-8 -*-
"""MultiLinearRegreesionAss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sz8myhd5rYKEeafoAIcxX8a_jRcusrIe

Prepare a prediction model for profit of 50_startups data.
Do transformations for getting better predictions of profit and
make a table containing R^2 value for each prepared model.

R&D Spend -- Research and devolop spend in the past few years
Administration -- spend on administration in the past few years
Marketing Spend -- spend on Marketing in the past few years
State -- states from which data is collected
Profit  -- profit of each state in the past few years
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

data = pd.read_csv("/content/50_Startups.csv")
data.head()

data.info()

data1=data.rename({'R&D Spend':'RDS','Administration':'ADMS','Marketing Spend':'MKTS'},axis=1)
data1.head()

data1.duplicated()

"""Correlation Matrix"""

sns.heatmap(data1.corr(),annot=True,cmap='Blues')
plt.show()

"""Scatterplot between variables along with histograms"""

sns.set_style(style='darkgrid')
sns.pairplot(data1)

"""## **Preparing Model**"""

model=smf.ols("Profit~RDS+ADMS+MKTS",data=data1).fit()

model.params

print('*** t-values ***','\n',model.tvalues, '\n','*** p-values ***','\n',model.pvalues)

model.rsquared , model.rsquared_adj

"""# **Simple Linear Regression Model**"""

ml_r = smf.ols("Profit~RDS",data=data1).fit()
print(ml_r.tvalues,'\n',ml_r.pvalues)

ml_a = smf.ols("Profit~ADMS",data=data1).fit()
print(ml_a.tvalues,'\n',ml_a.pvalues)

ml_ = smf.ols("Profit~ADMS",data=data1).fit()
print(ml_a.tvalues,'\n',ml_a.pvalues)





