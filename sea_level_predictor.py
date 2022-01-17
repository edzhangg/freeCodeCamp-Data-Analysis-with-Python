import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years1 = list(range(1880, 2051))
    seaLevel1 = list()
    counter = 0
    for i in years1:
      seaLevel1.append(line1.intercept + (line1.slope * years1[counter]))
      counter += 1
    plt.plot(years1, seaLevel1)

    # Create second line of best fit
    df_newline = df[df["Year"] >= 2000]
    line2 = linregress(df_newline["Year"], df_newline["CSIRO Adjusted Sea Level"])
    years2 = list(range(2000, 2051))
    seaLevel2 = list()
    counter = 0
    for j in years2:
      seaLevel2.append(line2.intercept + (line2.slope * years2[counter]))
      counter += 1
    plt.plot(years2, seaLevel2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()