import numpy as np


def smooth(rough, halfWindow):
    smoothed = np.copy(rough)
    windowFactor = (1 + 0.5 * np.arange(-halfWindow, halfWindow + 1)**2) ** -1
    for i in range(len(smoothed)):
        if i < halfWindow or len(smoothed) - i < halfWindow + 1:
            continue
        slice = rough[i - halfWindow : i + halfWindow + 1]
        smoothed[i] = sum(windowFactor * slice)/sum(windowFactor)
    return smoothed
