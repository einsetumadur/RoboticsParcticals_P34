import pandas as pd
import numpy as np
from scipy.signal import correlate

column_names = ["Curr_Target [mA]", "Curr_Measure [mA]", "Pos_Target [°]", "Pos_Measure [°]", "V_Cmd"]

def load_data(path):
    # load data from csv file, replace header row with column names and drop column 5, data is float
    data = pd.read_csv(path, header=None, names=column_names).dropna()
    # convert data to float
    data = data.apply(pd.to_numeric, errors='coerce')
    # drop rows with NaN values
    data = data.dropna()
    # reset index
    data = data.reset_index(drop=True)
    return data


def align_measurements(measurements, degree):   
    jump = 90-degree
    indexs = [np.where(measurement[column_names[2]].to_numpy() == -jump)[0][0] for measurement in measurements]
    shifts = [indexs[0] - index for index in indexs]
    biggest_shift = max(shifts)
    
    # shift all measurements to the first one
    for i, shift in enumerate(shifts):
        measurements[i] = measurements[i].shift(periods=shift)
        # remove biggest_shift rows from the beginning
        measurements[i] = measurements[i].iloc[biggest_shift:]
    
    # crop all measurements to the same length
    min_length = min([len(measurement) for measurement in measurements])
    for i in range(len(measurements)):
        measurements[i] = measurements[i].iloc[:min_length]
        
    return measurements