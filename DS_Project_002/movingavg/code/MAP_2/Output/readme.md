# Time Series

Time series is a sequence of information which attaches a time period to each value.
The value can be pretty much anything measurable.
It depends on time in some way, like prices, humidity or number of people.
As long as the values we record are unambiguous, any medium could be measured with Time series.
There aren't any limitations regarding the total time span of our Time series.
It could be a minute, a day, a month or even a century.
All we need is a starting and an ending point.

## Moving Average 

A moving average is a calculation used to analyze data points by creating averages of different subsets of the full data set in series.

- Moving averages are a simple and common type of smoothing used in time series analysis and time series forecasting. 
- Calculating a moving average involves creating a new series where the values are comprised of the average of raw observations in the original time series
- Calculating a moving average of a time series takes some assumptions on data. 
- It is assumed that both trend and seasonal components have been removed from your data.
- This means that your time series is stationary, or does not show obvious trends (long-term increasing or decreasing movement) or seasonality (consistent periodic structure).
- This repository contains the code files for moving average prediciton on a time series data.

## Basics

-  Chronological Data
- Cannot be shuffled
- Each row indicate specific time record
- Train – Test split happens chronologically
- Data is analyzed univariately (for given use case)
- Nature of the data represents if it can be predicted or not


## Folder Sturcture Info:

* Clone the repository
* "Input" folder contains input csv files
* "MLPipeline" folder contains python files needed for moving average
* "Notebooks" folder contains ipynb files
* "Output" folder contains the charts and plots created during the process


## Code Description

    File Name : Config.py
    File Description : Class to set the constant values


    File Name : Engine.py
    File Description : Main class for starting different parts and processes of the lifecycle


    File Name : EDA.py
    File Description : Class to do all the EDA over the time series data


    File Name : MovingAverage.py
    File Description : Class to do the moving average operations


    File Name : Resampling.py
    File Description : Class to perform resampling of code


## Steps to Run

There are two ways to execute the end to end flow.

- Modular Code
- IPython

### Modular code

- Create virtualenv
- Install requirements `pip install -r requirements.txt`
- Run Code `python Engine.py`
- Check output for all the visualization

### IPython Google Colab

Follow the instructions in the notebook `MovingAverage.ipynb`

