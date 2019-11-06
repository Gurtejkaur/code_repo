import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import scikitlearn
from scikitlearn import preprocessing
from scikitlearn.preprocessing import scale

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch03/03_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars.mpg
mpg_matrix = mpg.reshape(-1,1)
help(mpg_matrix)
