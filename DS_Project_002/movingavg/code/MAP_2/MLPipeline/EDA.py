import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt


def print_data_info(self):
        
        print(self.time_series.head())
        print(self.time_series.shape)  # Number of Observations
        print(self.time_series.loc["2017-08-30"])  # Querying By Time
        print(self.time_series.describe())  # Descriptive Statistics


def date_refactor(self): 

        df = pd.DataFrame()
        df['month'] = [self.time_series.index[i].month for i in
                       range(len(self.time_series))]  # Extract month
        df['day'] = [self.time_series.index[i].day for i in
                     range(len(self.time_series))]  # Extract day
        df['hour'] = [self.time_series.index[i].hour for i in
                      range(len(self.time_series))]  # Extract hour 
        df["sensoryVale"] = [self.time_series.Sensor_Value.iloc[i] for i in 
                             range(len(self.time_series))]
        # Year attribute is discarded since there is no variation in the data
        print("Years present: \t", set([self.time_series.index[i].year for i in
                                        range(len(self.time_series))]))
        print(df.head())

        return df


def visualize_distributions(self):
       
        date_info_df = date_refactor(self)
        print(date_info_df.columns)
        for col in date_info_df.columns[:-1]: 
            sns.countplot(data=date_info_df, x=col)
            plt.title(str(col).upper()+" Distribution")
            plt.xticks(rotation=45)
            plt.savefig(f"{self.output_folder}+{col}.png")
            plt.close()

        # Make the data one dimensional for GROUPER
        data = \
            pd.DataFrame(columns=["Sensor_Value"],data=self.time_series["Sensor_Value"])
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
        self.time_series.hist(figsize=(20, 10))
        plt.savefig(f"{self.output_folder}+Histogram of all columns.png")
        plt.close()


def plot_values(self):
       
        # Density Plots
        self.time_series.plot(kind='kde', figsize=(20, 10))
        plt.savefig(f"{self.output_folder}+Density Plots.png")
        plt.close()

        pd.plotting.lag_plot(self.time_series)
        plt.savefig(f"{self.output_folder}+Lag Plot.png")
        plt.close()

        # QQPlot
        sm.qqplot(self.time_series["Sensor_Value"])
        plt.savefig(f"{self.output_folder}+QQPlot.png")
        plt.close()

        # Check for missing values in predictor variable (Sensor_Value)
        print(self.time_series["Sensor_Value"].isna().sum())
