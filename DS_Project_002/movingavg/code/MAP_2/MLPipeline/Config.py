import pandas as pd

# create a class for basic configurations
class IOConfig:

    data_folder = "movingavg/code/MAP_2/Input/Data-Chillers.csv"
    output_folder = "movingavg/code/MAP_2/Output/"

    series = pd.read_csv(data_folder, header=0, index_col=0, parse_dates=True, squeeze=True)

    print(series.head())

    #### Number of Observations
    print(series.shape)

    ####  Querying By Time
    print(series["2017-08-30"])

    #### Descriptive Statistic
    print(series.describe())

