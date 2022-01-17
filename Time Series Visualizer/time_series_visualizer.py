import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                index_col="date",
                parse_dates=True)

# Clean data
df = df[((df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975)))]

def draw_line_plot():
    # Draw line plot
    plots = df.plot(color="red", xlabel="Date", ylabel="Page Views", figsize=(10, 5))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig = plots.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame()
    df_bar["year"] = df.index.year
    df_bar["Months"] = df.index.month
    df_bar["value"] = df.values
    df_bar = df_bar.groupby(["year", "Months"])["value"].mean().reset_index()
    df_bar = df_bar.sort_values(["year", "Months"])
    df_bar["Months"] = pd.to_datetime(df_bar["Months"], format="%m").dt.month_name()

    # Draw bar plot
    plots = sns.catplot(data=df_bar, kind="bar", x="year", y="value", hue="Months", hue_order=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], legend_out=False)
    plots.fig.set_figheight(6)
    plots.fig.set_figwidth(9)
    plots.set_axis_labels("Years", "Average Page Views")
    fig = plots.fig

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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
    sns.boxplot(ax=ax1, x="year", y="value", data=df_box)
    sns.boxplot(ax=ax2, x="month", y="value", data=df_box, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
