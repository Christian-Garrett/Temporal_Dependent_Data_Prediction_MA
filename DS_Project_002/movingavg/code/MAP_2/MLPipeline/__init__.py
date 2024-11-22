from pathlib import Path
import os
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))


class DataPipeline:
    """
    A class used to create the data pipeline.
    ...

    Attributes
    ----------
    data_folder : str
        Time series input data text path
    output_folder : str
        Time series output data text path
    time_series : df
        Time series input data
    predictions : list
        Moving average predictions
    test : list
        Moving average test data

    Methods
    -------
    preprocess_data()
        Load data, set index, change formats, visual sanity checks.
    perform_EDA()
        Check for stationarity, examine autocorrelation attributes.
    train_model()
        Implement the moving average model and get predictions.
    evaluate_model()
        RMSE model evaluation and plot prediction deviations.

    """

    from MLPipeline.EDA import (print_data_info, 
                                visualize_distributions,
                                plot_values)
    from MLPipeline.Resampling import resampling_visualizations
    from MLPipeline.MovingAverage import (get_moving_average_preds,
                                          plot_predictions)

    def __init__(self, data_path, output_path="Output/"):

        self.output_folder=os.path.join(module_path, output_path)
        self.data_folder=os.path.join(module_path, data_path)
        self.time_series = pd.read_csv(self.data_folder,
                                       dayfirst=True,
                                       header=0, 
                                       index_col=0, 
                                       parse_dates=True)  
        self.time_series = \
            self.time_series.iloc[:, 0] \
                if self.time_series.shape[1] == 1 else self.time_series
        self.predictions=None
        self.test=None

    def preprocess_data(self):
        
        self.print_data_info()
        print("This completes Preprocessing")

    def perform_EDA(self):

        self.visualize_distributions()
        self.plot_values()
        self.resampling_visualizations()
        print("This completes EDA")

    def train_model(self):

        self.get_moving_average_preds()
        print("This completes model training")

    def evaluate_model(self):

        rmse = np.sqrt(mean_squared_error(self.test, self.predictions))
        print('Test RMSE: %.3f' % rmse)
        self.plot_predictions()
        print("This completes model evaluation")
