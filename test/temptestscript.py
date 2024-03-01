import sys
sys.path.append(r"D:\document\statistics\TidyStatsProject")
from EasySeaborn import ecdf
import matplotlib.pyplot as plt
from SoEasyData import GetSeabornData
import numpy as np
titanic = GetSeabornData("titanic")
flights = GetSeabornData("flights")
ax = ecdf(titanic, groupby="survived", xvarname="age", ecdfparamsdict={"iscomplementary": 1}, savefilename="./image/ecdf91.png", block=False)
plt.pause(2)
plt.close()
ax = ecdf(titanic, groupby="survived", xvarname="age", ecdfparamsdict={"iscomplementary": 0}, savefilename="./image/ecdf92.png", block=False)
plt.pause(2)
plt.close()
