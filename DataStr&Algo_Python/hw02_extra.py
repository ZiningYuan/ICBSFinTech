#####
# Test with actual stock data using pandas datareader

import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
from datetime import datetime
from hw02 import moving_average, compare_mas, ma_strategy, buy_and_hold

def get_stock(symbol, start, end):
    """
    Downloads stock price data from Yahoo
    Returns a pandas dataframe.
    """
    df = pdr.DataReader(symbol, 'yahoo', start, end)
    df = df.sort_index(axis=0)
    return df


def get_close(df):
    """
    Returns stock price dataframe's adjusted closing price as a list
    """
    l = df['Adj Close'].values.tolist()
    return l


def ma_vs_buyandhold(n1, n2, prices, starting_money):
    """
    Performs comparison between moving average crossover strategy and buy and hold
    
    Assume n1 < n2
    """

    # Moving averages
    ma1 = moving_average(prices, n1)
    ma2 = moving_average(prices, n2)

    # Crossovers
    cos = compare_mas(ma1, ma2)

    # Make trades using crossover strategy, get list of values
    ma_values = ma_strategy(prices, cos, starting_money)

    # Get buy and hold strategy values
    
    # Buy and hold
    bh_values = buy_and_hold(prices, n2-1, starting_money)

    print("Buy and hold: " + str(bh_values[-1]))
    print("Crossover MA: " + str(ma_values[-1]))

    return [bh_values, ma_values]


def plot_ma(stock_code='AMZN'):
    """
    Calculates moving average strategy on ticker values and plots results

    Assumes you can trade the ticker like a stock
    
    Assumes zero trading costs
    """
    
    # Initialize MA strategy for n1 and n2 length moving averages in specified time period
    n1 = 20
    n2 = 50
    start = datetime(2010, 1, 1)
    finish = datetime(2018, 6, 30)
    starting_money = 1000
    
    # Download stock prices (adjusted daily closing prices)
    stock = get_stock(stock_code, start, finish)
    prices = get_close(stock)
    
    # Trading comparison
    values = ma_vs_buyandhold(n1, n2, prices, starting_money)
    
    # Plotting
    plt.plot(values[0])
    plt.plot(values[1])
    plt.legend(['BH', 'MA'])

