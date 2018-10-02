# Urbana Champaign Sewage Collection System

## Inspiration
This project was inspired by one of PYGHack's available data sets. By identifying the specific lift stations where the most inflow and infiltration (I&I) is entering during a rainstorm event, leak detection/remediation efforts can be focused on the subsections of the collections system that feed into these lift stations.

## What it does
The project analyzes the correlation between precipitation levels and inflow levels. For every lift, the graphs of (Precipitation vs Time) and (Inflow vs Time) are overlayed, and then (Inflow vs Precipitation) is graphed as a scatter plot. By calculating the slope of a linear regression for this scatter plot, we can determine how much the inflow to that lift increases per 1.0 inch increase in precipitation, which is a decent measure of vulnerability.

Note that the inflow is measured in multiples of dry-day inflow, which helps normalize vulnerability across all lifts. Also, scatter plots with very low r-value (< 0.4) are ignored because that means the correlation between precipitation and inflow isn't actually strong enough for the linear regression to be meaningful.

## How I built it
The parsing and processing of data was done with Python and NumPy, and the data visualization was done with Matplotlib. I implemented my own data smoothing function, which replaces each value (for precipitation or inflow) with a weighted average of the values in a window around the original value. This creates a much stronger correlation, because sometimes the inflow doesn't react to changes in precipitation immediately.

## Results

Lifts which are very vulnerable to inflow include Timber Hills, O_ L_ Johnson, and Bradley McKinley. Slightly less vulnerable lifts include East Main, Perkins, and Broadway.

See All_Plots.pdf for a lot of pretty graphs!

https://github.com/jasonxia17/urbana-champaign-sewage-collection-system/blob/master/All_Plots.pdf

## Potential Improvements to Analysis

Currently, the precipitation value for any given date is calculated as the average of the measurements from all weather stations in the Champaign-Urbana station. A more through analysis could use the precipitation measurement from the closest station to a lift when analyzing that lift's data.
