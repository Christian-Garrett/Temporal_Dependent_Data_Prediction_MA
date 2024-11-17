import pandas as pd
from pathlib import Path
import sys
import os

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

# create a class for basic configurations
class IOConfig:

    data_folder = os.path.join(module_path, "Input/Data-Chillers.csv")
    output_folder = os.path.join(module_path, "Output/")

    # Read the CSV file without using the deprecated `squeeze` parameter
    series = pd.read_csv(data_folder, header=0, index_col=0, parse_dates=True)

    # If the resulting DataFrame has only one column, convert it to a Series
    if series.shape[1] == 1:
        series = series.iloc[:, 0]

    print(series.head())

    #### Number of Observations
    print(series.shape)

    ####  Querying By Time
    print(series.loc["2017-08-30"])

    #### Descriptive Statistic
    print(series.describe())
