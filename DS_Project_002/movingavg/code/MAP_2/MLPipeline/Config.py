import pandas as pd
from pathlib import Path
import sys
import os

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))

class IOConfig:
    """
    A class used to configure the pipeline modules.

    Attributes:
        data_folder (str): The input data file.
        output_folder (str): The output file location.
        time_series (df): The input dataframe with sensor and error values.
    """

    data_folder = os.path.join(module_path, "Input/Data-Chillers.csv")
    output_folder = os.path.join(module_path, "Output/")

    # Read the CSV file without using the deprecated `squeeze` parameter
    time_series = pd.read_csv(data_folder, header=0, index_col=0, parse_dates=True)

    # If the resulting DataFrame has only one column, convert it to a Series
    if time_series.shape[1] == 1:
        time_series = time_series.iloc[:, 0]
