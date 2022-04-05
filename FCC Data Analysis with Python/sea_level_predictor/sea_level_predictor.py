import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig = plt.figure(figsize=(14, 6))
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level' )


    # Create first line of best fit
    all_proj = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = all_proj.slope
    b = all_proj.intercept
    x = np.array(range(min(df['Year']), 2051))
    # plt.plot(df['Year'], m * df['Year'] + b )
    plt.plot(x, m * x + b)


    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    proj_future = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    m = proj_future.slope
    b = proj_future.intercept
    x = np.array(range(2000, 2051))
    plt.plot(x, m * x + b)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()