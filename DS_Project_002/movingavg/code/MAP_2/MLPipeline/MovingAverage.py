import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_moving_average_preds(self):

    data = pd.DataFrame(columns=["Sensor_Value"],
                        data=self.time_series["Sensor_Value"])
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
        # print('predicted=%f, expected=%f' % (yhat, obs))

    self.predictions=predictions
    self.test=test


def plot_predictions(self):

    # plotting
    plt.plot(self.test)
    plt.plot(self.predictions, color='red')
    plt.savefig(f"{self.output_folder}+Moving Average.png")
    plt.close()

    # zoom plot
    plt.plot(self.test[:100])
    plt.plot(self.predictions[:100], color='red')
    plt.savefig(f"{self.output_folder}+Moving Average (Close Look).png")
    plt.close()
