def floatParse(potentialFloat):
    try:
        return float(potentialFloat)
    except ValueError:
        return 0

def averageSameDate(inputData):
    outputData = []
    prevDate = inputData[0][0]
    valuesOnDate = []
    for currentDate, value in inputData + [(None, None)]: # Hack which allows last date to be processed
        if currentDate != prevDate:
            outputData.append((prevDate, np.average(valuesOnDate)))
            prevDate = currentDate
            valuesOnDate = [value]
        else:
            valuesOnDate.append(value)
    return outputData

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Influent Flow (MGD)', color=color)
ax1.plot(flowDict.keys(), flowDict.values(), color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Precipitation (inches)', color=color)  # we already handled the x-label with ax1
ax2.plot(pptDict.keys(), pptDict.values(), color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()