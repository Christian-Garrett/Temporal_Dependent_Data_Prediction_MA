from pathlib import Path
import sys
import os

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

from MLPipeline.EDA import EDA
from MLPipeline.MovingAverage import MovingAverage
from MLPipeline.Resampling import Resampling
import pandas as pd


# Loading the dataset
df = pd.read_csv(os.path.join(module_path, "Input/Data-Chillers.csv"))

# Convert the time from string to date format
df.time = pd.to_datetime(df.time, format='%d-%m-%Y %H:%M')

# Set time column as the index
df.set_index("time", inplace=True)

# Perfrom Exploratory Data Analysis(EDA)
eda = EDA(df)
eda.run_EDA()

# Perform resampling on data
resampling = Resampling(df)
resampling.run_resampling()

# Perform moving average smoothing
movingaverage = MovingAverage(df)
movingaverage.run_movingaverage()

print("Completed Moving Average")
