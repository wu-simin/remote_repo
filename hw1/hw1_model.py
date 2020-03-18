import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('hw1/train.csv','r',encoding='Big5',index_col=False,delimiter=',')
print(train_data)
rows = np.size(train_data,0)
Pm = []
