import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from datetime import datetime


def overlayPrecipAndFlow(liftName, dates, precips, inflowsNormed):
    fig, ax1 = plt.subplots(figsize=(11,8.5))

    ax1.set_title(liftName)

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Precipitation (inches)', color=color)
    ax1.plot(dates, precips, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Inflow \n\n (as a multiple of dry-day inflow)', color=color)
    # we already handled the x-label with ax1
    ax2.plot(dates, inflowsNormed, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.xlim(datetime(2015,1,1), datetime(2017,1,1))

    #fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig('Plots\\' + liftName + ' Overlay')
    plt.close()

def scatterPrecipVsFlow(liftName, precips, inflowsNormed):
    slope, intercept, r_value, p_value, std_err = stats.linregress(precips, inflowsNormed)
    bfLineX = np.linspace(np.amin(precips), np.amax(precips))
    bfLineY = slope * bfLineX + intercept

    fig, ax = plt.subplots(figsize=(11,8.5))
    ax.scatter(precips, inflowsNormed, s=2)
    ax.plot(bfLineX, bfLineY, color='red')

    ax.set_title(liftName + '\n\n Precipitation Vulnerability: ' + str(round(slope, 2))
                 + '\nCorrelation: ' + str(round(r_value,3)))
    ax.set_xlabel('Precipitation (inches)')
    ax.set_ylabel('Inflow \n\n (as a multiple of dry-day inflow)')
    plt.ylim(0, 4)

    #fig.tight_layout()
    plt.savefig('Plots\\' + liftName + ' Scatter')
    plt.close()