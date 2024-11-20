import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from .Config import IOConfig

# create a class for moving average smoothing
class MovingAverage(IOConfig):
    """
    A class used to perform moving average smoothing.
    ...

    Attributes
    ----------
    series : df
        Time series input data.

    Methods
    -------
    run_movingaverage()
        Create a dataframe to isolate important time attributes.

    """

    def __init__(self, time_series):
        """
        Initializes the MovingAverage object.

        Parameters
        ----------
        time_series : df
            Input time series sensor data.
            
        """
        self.series = time_series

    def run_movingaverage(self):
        """
        Calculating a moving average of a time series takes some assumptions on data. 
        It is assumed that both trend and seasonal components have been removed from 
        the data. This means that the time series is stationary, or does not show 
        obvious trends (long-term increasing or decreasing movement) or seasonality 
        (consistent periodic structure). There are many methods to remove trends and 
        seasonality from a time series dataset when forecasting. Two methods for each 
        are to use the differencing method and to model the behavior and explicitly 
        subtract it from the series.

        """

        data = pd.DataFrame(columns=["Sensor_Value"],data=self.series["Sensor_Value"])
        rolling = data.rolling(window=3)
        rolling_mean = rolling.mean()
        print(rolling_mean.head(10))

        # plot original and transformed dataset
        data.plot()
        rolling_mean.plot(color='red')
        plt.savefig(f"{self.output_folder}+Resampled.png")
        plt.close()

        # zoomed plot original and transformed dataset
        data[:100].plot()
        rolling_mean[:100].plot(color='red')
        plt.savefig(f"{self.output_folder}+Resampled (Close Look).png")
        plt.close()

        # moving Average of window 3
        df = data.copy()
        width = 3
        lag1 = df.shift(1)
        lag3 = df.shift(width - 1)
        window = lag3.rolling(window=width)
        means = window.mean()
        dataframe = pd.concat([means, lag1, df], axis=1)
        dataframe.columns = ['mean', 't', 't+1']
        print(dataframe.head(10))

        # mathematical function to make prediction based on Moving average
        data_vals = data.values
        window_size = 3
        history = [data_vals[i] for i in range(window_size)]
        test = [data_vals[i] for i in range(window_size, len(data_vals))]
        predictions = list()
        # walk forward over time steps in test
        for t in range(len(test)):
            length = len(history)
            yhat = np.mean([history[i] for i in range(length-window_size, 
                                                      length)])
            obs = test[t]
            predictions.append(yhat)
            history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
        rmse = np.sqrt(mean_squared_error(test, predictions))
        print('Test RMSE: %.3f' % rmse)

        # plotting
        plt.plot(test)
        plt.plot(predictions, color='red')
        plt.savefig(f"{self.output_folder}+Moving Average.png")
        plt.close()

        # zoom plot
        plt.plot(test[:100])
        plt.plot(predictions[:100], color='red')
        plt.savefig(f"{self.output_folder}+Moving Average (Close Look).png")
        plt.close()

        print("This completes Moving Average")
