# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:10:38 2021

@author: jpalominogo
"""
import pandas as pd
df = pd.read_excel('example.xlsx', sheet_name='example')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import attrgetter
#pip install pmdarima
from pmdarima.arima import auto_arima
from math import sqrt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
#pip install pystan
#conda install -c conda-forge fbprophet
from fbprophet import Prophet
