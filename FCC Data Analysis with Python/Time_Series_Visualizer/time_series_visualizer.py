import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# import datetime as dt # not part of the assignment



# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# df = pd.read_csv('fcc-forum-pageviews.csv',index_col = 'date')

df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True, drop=True)


# Clean data

df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]







def draw_line_plot():
    # Draw line plot
    # df.plot(kind='line', figsize=(14, 6))

    fig = plt.figure(figsize=(14, 6))
    plt.plot(df, 'r')
    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # df_bar = df.copy()
    # df_bar['Year'] = df_bar.index.year.values #retrieve year from the index then create column
    # df_bar['Months'] = df_bar.index.month.values

    # ALTERNATIVE, change the month numbers to strings
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year.values  # retrieve year from the index then create column
    df_bar['Months'] = df_bar.index
    df_bar['Months'] = df_bar['Months'].dt.month_name()


    # # Draw bar plot
    # fig = plt.figure(figsize=(10, 6))
    # plt.bar(x=df_bar['Year'], height=df_bar['value'])
    # plt.title('Sales over time')
    # plt.xlabel('year')
    # plt.ylabel('Sales')
    # plt.show()
    #
    # labels = ["2016", "2017", "2018", "2019"]
    # fig = plt.figure(figsize=(10, 6))
    # plt.bar(x=df_bar['Year'], height=df_bar['value'])
    # plt.xticks(df_bar['Year'], labels, rotation='vertical')
    # plt.title('Sales over time')
    # plt.xlabel('year')
    # plt.ylabel('Sales')
    # plt.show()


    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=df_bar, x = 'Year', y='value', hue = "Months", hue_order = ['January', 'February', 'March',
                                   'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel("Years")
    plt.ylabel('Average Page Views')






    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1,2, figsize=(16,8))
    # plt.setp(ax, yticks=[0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    sns.boxplot(data=df_box, x = 'year', y='value', ax = ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)" )
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    # ax[0].set_ylim([0, 200000])


    sns.boxplot(data=df_box, x='month' ,y='value', ax=ax[1], order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                                                                      'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    # ax[1].set_ylim([0, 200000])



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
