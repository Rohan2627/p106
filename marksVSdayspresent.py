import pandas as pd
import csv
import plotly_express as pe 

import numpy as np

data = pd.read_csv("marksVSdayspresent.csv")

marks = data["Marks In Percentage"].tolist()
dp = data["Days Present"].tolist()

graph = pe.scatter(data, x = marks, y = dp)
graph.show()


correlation = np.corrcoef( data["Marks In Percentage"] , data["Days Present"] )

print("Correlation coefficient in between sleep and cup of coffees : " , correlation[0,1])







