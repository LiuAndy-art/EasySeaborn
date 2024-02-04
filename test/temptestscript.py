import sys
sys.path.append(r"D:\document\statistics\TidyStatsProject")
from EasySeaborn import box
import matplotlib.pyplot as plt
from SoEasyData import GetSeabornData
import numpy as np
titanic = GetSeabornData("titanic")
flights = GetSeabornData("flights")
print(flights)
ax = box(titanic, xvarname="deck", yvarname="age", boxparamsdict={"isshowmean": 1, "meanlinecolor": "green", "meanlinewidth": 1.2}, savefilename="./image/box111.png", block=False)
plt.pause(2)
plt.close()
