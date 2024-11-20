import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
from .Config import IOConfig

class EDA(IOConfig):
    """
    A class used to perform the exploratory data analysis.
    ...

    Attributes
    ----------
    series : df
        Time series input dataframe with sensor and error values.

    Methods
    -------
    date_refactor()
        Create a dataframe to isolate important time attributes.
    run_EDA()
        Run the EDA section of the data pipeline.

    """
    
    def __init__(self, time_series):
        """
        Initializes the EDA object.

        Parameters
        ----------
        time_series : df
            Input time series sensor data.
            
        """

        self.series = time_series

        print(self.series.head())
  
        print(self.series.shape)  # Number of Observations

        print(self.series.loc["2017-08-30"])  # Querying By Time
    
        print(self.series.describe())  # Descriptive Statistics


    def date_refactor(self): 
        """
        Create a dataframe to isolate important time attributes.

        Returns
        -------
        df
            A dataframe with a column for each month, day, hour and 
            sensor value.
            
        """

        df = pd.DataFrame()
        df['month'] = [self.series.index[i].month for i in
                       range(len(self.series))]  # Extract month
        df['day'] = [self.series.index[i].day for i in
                     range(len(self.series))]  # Extract day
        df['hour'] = [self.series.index[i].hour for i in
                      range(len(self.series))]  # Extract hour 
        df["sensoryVale"] = [self.series.Sensor_Value.iloc[i] for i in 
                             range(len(self.series))]
        # Year attribute is discarded since there is no variation in the data
        print("Years present: \t", set([self.series.index[i].year for i in
                                        range(len(self.series))]))
        print(df.head())

        return df
    

    def run_EDA(self):
        """
        Run the EDA section of the pipeline.
            
        """
        date_info_df = self.date_refactor()

        print(date_info_df.columns)
        for col in date_info_df.columns[:-1]: # Visualizing the distribution of all the columns
            sns.countplot(data=date_info_df, x=col)
            plt.title(str(col).upper()+" Distribution")
            plt.xticks(rotation=45)
            plt.savefig(f"{self.output_folder}+{col}.png")
            plt.close()

        # Make the data one dimensional for GROUPER
        data = pd.DataFrame(columns=["Sensor_Value"],data=self.series["Sensor_Value"])
        print(data.head(3))

        # Get the months distribution of sensory data
        groups = data.groupby(pd.Grouper(freq='M'))
        weeks = pd.DataFrame()
        for name, group in groups:
            # The print stmt shows the number of data points for each months differs, 
            # so it was standardized to 53 data points (lowest from all months considered)
            print(name.month, "-",group.Sensor_Value.nunique())
            weeks[name.month] = list(group.Sensor_Value)[:53] 

        weeks.plot(subplots=True,legend=True, figsize=(25, 25) )
        plt.savefig(f"{self.output_folder}+Each Month Distribution.png")
        plt.close()

        # Histogram Plot For Distribution
        self.series.hist(figsize=(20, 10))
        plt.savefig(f"{self.output_folder}+Histogram of all columns.png")
        plt.close()

        # Density Plots
        self.series.plot(kind='kde', figsize=(20, 10))
        plt.savefig(f"{self.output_folder}+Density Plots.png")
        plt.close()

        pd.plotting.lag_plot(data)
        plt.savefig(f"{self.output_folder}+Lag Plot.png")
        plt.close()

        # QQPlot
        sm.qqplot(data["Sensor_Value"])
        plt.savefig(f"{self.output_folder}+QQPlot.png")
        plt.close()

        # Check for missing values in predictor variable (Sensor_Value)
        print(data["Sensor_Value"].isna().sum())

        print("This completes EDA")
