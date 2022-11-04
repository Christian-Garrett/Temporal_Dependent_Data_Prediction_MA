from movingavg.code.MAP_2.MLPipeline.EDA import EDA
from movingavg.code.MAP_2.MLPipeline.MovingAverage import MovingAverage
from movingavg.code.MAP_2.MLPipeline.Resampling import Resampling
import pandas as pd

# Loading the dataset
df = pd.read_csv("movingavg/code/MAP_2/Input/Data-Chillers.csv")

# Convert the time from string to date format
df.time = pd.to_datetime(df.time, format='%d-%m-%Y %H:%M')

# Set time column as the index
df.set_index("time", inplace=True)

# Perfrom Exploratory Data Analysis(EDA)
eda = EDA(df)
eda.RunEDA()

# Perform Resampling on data
resampling = Resampling(df)
resampling.RunResampling()

# Perform moving average smoothing
movingaverage = MovingAverage(df)
movingaverage.RunMovingAverage()

print("Completed Moving Average")
