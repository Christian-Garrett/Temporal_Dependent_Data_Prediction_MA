import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from .Config import  IOConfig


class Resampling(IOConfig):
    """
    A class used to resample the time series data.
    ...

    Attributes
    ----------
    series : df
        Time series input data.

    Methods
    -------
    run_resampling()
        Create a dataframe to isolate important time attributes.

    """

    def __init__(self, time_series):
        """
        Initializes the Resampling object.

        Parameters
        ----------
        time_series : df
            Input time series sensor data.
            
        """
        self.series = time_series

    def run_resampling(self):
        '''
        There are two kinds of resampling, they are upsampling and downsampling
        Since this data has missing record we would upsample and interpolate the 
        values for those data points.

        '''

        data = pd.DataFrame(columns=["Sensor_Value"],data=self.series["Sensor_Value"])

        # Identify the missing days and fill them up with "NAN"
        upsampled = data.resample('D').mean()
        print("No of days : \t",upsampled["Sensor_Value"].isna().sum())

        # Calculating the number of hours missing from the dataset
        upsampled = data.resample('H').mean()
        print("No of hours missing : \t",upsampled["Sensor_Value"].isna().sum())

        upsampled = data.resample('D').mean()
        print("Overall data points : \t",upsampled.shape)

        print(upsampled.head(5)) 

        # Linear setting draws a straight line between available data
        interpolated = upsampled.interpolate(method='linear') 
        print(interpolated.head(5))
        interpolated.plot()
        plt.savefig(f"{self.output_folder}+Interploted Plot (linear).png")
        plt.close()

        # Polynomial function with order 1
        interpolated = upsampled.interpolate(method="spline", order=1) 
        print(interpolated.head(5))
        interpolated.plot()
        plt.savefig(f"{self.output_folder}+Interploted Plot (spline).png")
        plt.close()

        # Examining the data again before final transformations
        plt.figure(1)
        # line plot
        plt.subplot(211)
        plt.plot(data)
        # histogram
        plt.subplot(212)
        plt.hist(data["Sensor_Value"])
        plt.savefig(self.output_folder + "/Before transformations+.png")
        plt.close()

        #### Square Root Transform
        '''
        It is possible that our dataset shows a quadratic growth. In that case, 
        then we could expect a square root transform to reduce the growth trend to 
        be linear and change the distribution of observations to nearly Gaussian type.

        '''

        transform = np.sqrt(data)
        plt.figure(1)
        # line plot
        plt.subplot(211)
        plt.plot(transform)
        # histogram
        plt.subplot(212)
        plt.hist(data["Sensor_Value"])
        plt.savefig(self.output_folder + "/Square Root Transformation Histogram+Line.png")
        plt.close()

        #### Log Transform
        '''
        This method is popular among time series data as they are effective at removing 
        exponential variance. It assumes values are positive and non-zero. It is common 
        to transform observations by adding a fixed constant to ensure all input values meet 
        this requirement.
                transform = log(constant + x)

        '''
        copied_data = data.copy()
        copied_data['log_Sensor_Value'] = np.log(copied_data['Sensor_Value'])
        plt.figure(1)
        # line plot
        plt.subplot(211)
        plt.plot(copied_data['Sensor_Value'])
        # histogram
        plt.subplot(212)
        plt.hist(copied_data['Sensor_Value'])
        plt.savefig(self.output_folder + "/Log Transformation Histogram+Line.png")
        plt.close()

        # BOX COX Transform
        '''
        The square root transform and log transform belong to a class of transforms called power 
        transforms. The Box-Cox transform2 is a configurable data transform method that supports 
        both square root and log transform, as well as a suite of related transforms. Box-Cox 
        transform only takes predictor variable which is positive integers. Since our data has 
        negative value we would scale our data and apply it to BOX-COX Transform

        From this we can infer that if we scale our data then we will get 0.0 for all the values
        hence we cannot perform Box-Cox Transform on this data.
        
        '''
        data_copy = data.copy()
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler.fit([data_copy["Sensor_Value"].tolist()])
        data_copy["Scaled_Sensor_Value"] = scaler.transform([data_copy["Sensor_Value"].tolist()])[0]
        set(scaler.transform([data_copy["Sensor_Value"].tolist()]).tolist()[0]) 
        ''''
        box, lam = boxcox(data_copy['Scaled_Sensor_Value'])
        pyplot.figure(1)
        #line plot
        pyplot.subplot(211)
        pyplot.plot(data_copy['box_cox_Sensor_Value'])
        # histogram
        pyplot.subplot(212)
        pyplot.hist(data_copy['box_cox_Sensor_Value'])
        pyplot.show()
        '''

        #### Moving Average Smoothing
        '''Centered Moving Average
        At time (t), it is calculated as the average of actual observations at, before, and after (t). 
        For example, a center moving average with a window of 3 would be calculated as:
        center_ma(t) = mean(obs(t - 1), obs(t), obs(t + 1))

        Trailing Moving Average
        At time (t), it is calculated as the average of  actual observations at and before the time (t). 
        For example, a trailing moving average with a window of 3 would be calculated as:
        trail_ma(t) = mean(obs(t - 2), obs(t - 1), obs(t))

        '''

        print("This completes Re-Sampling")
