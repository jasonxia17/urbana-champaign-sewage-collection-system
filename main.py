import csv
import numpy as np
from scipy import stats
from collections import OrderedDict
from datetime import datetime
from plotting import *

def parseTime(row):
    # Deals with all the different formats in DailyFlow.csv
    timeString = ",".join([row[0], row[1], row[2]]).lower().replace(".", "")
    possibleFormats = ['%B,%d,%Y', '%b,%d,%Y', '%bt,%d,%Y'] # stupid september
    for form in possibleFormats:
        try:
            return datetime.strptime(timeString, form)
        except ValueError:
            continue
    raise ValueError("This date doesn't fit any of the possible formats: ", row)

def unpackAndSmoothDicts(pptDict, flowDict):
    from smoothing import smooth
    dates = [date for date in flowDict if date in pptDict]
    precips = smooth(np.array([pptDict[date] for date in flowDict if date in pptDict]), halfWindow=5)
    inflows = smooth(np.array([flowDict[date] for date in flowDict if date in pptDict]), halfWindow=5)
    avgDryDayInflow = np.average([inflows[i] for i in range(len(inflows)) if precips[i] < 0.01])
    inflowsNormalized = inflows / avgDryDayInflow
    return dates, precips, inflowsNormalized, avgDryDayInflow

with open('ProcessedData\\Precipitation.csv') as file:
    pptDict = OrderedDict()
    # The value associated with each date key is a list of the precipitation readings on that day
    for row in list(csv.reader(file, delimiter='\t')):
        date = datetime.strptime(row[0], '%m/%d/%Y')
        precip = float(row[1])
        if date in pptDict:
            pptDict[date].append(precip)
        else:
            pptDict[date] = [precip]
    # Average all the readings taken at different stations on any given day
    for date in pptDict:
        pptDict[date] = np.average(pptDict[date])

with open('ProcessedData\\DailyFlow.csv') as file:
    flowDict = OrderedDict([(parseTime(row), float(row[3]))
                            for row in list(csv.reader(file, delimiter='\t'))])

dates, precips, inflowsNormed, avgDryDayInflow = unpackAndSmoothDicts(pptDict, flowDict)

overlayPrecipAndFlow('Cumulative', dates, precips, inflowsNormed)
scatterPrecipVsFlow('Cumulative', precips, inflowsNormed)

with open('ProcessedData\\LiftDailyFlow.csv') as file:
    liftDataDict = list(csv.DictReader(file, delimiter='\t'))
    liftList = list(liftDataDict[0].keys())[1:]

with open('LiftVulnerabilities.csv', mode='w') as file:
    file.write('Lift,Vulnerability,Correlation,Average Dry-Day Inflow (Gallons)\n')
    for liftName in liftList:
        flowDict = OrderedDict((datetime.strptime(row['Date'], '%m/%d/%Y'), float(row[liftName]))
                               for row in liftDataDict if row[liftName] != '0')
        dates, precips, inflowsNormed, avgDryDayInflow = unpackAndSmoothDicts(pptDict, flowDict)

        overlayPrecipAndFlow(liftName, dates, precips, inflowsNormed)
        scatterPrecipVsFlow(liftName, precips, inflowsNormed)

        slope, intercept, r_value, p_value, std_err = stats.linregress(precips, inflowsNormed)
        file.write(','.join([liftName, str(slope), str(r_value), str(avgDryDayInflow)]) + '\n')
