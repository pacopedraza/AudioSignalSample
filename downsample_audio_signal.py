#!/usr/bin/env python3

import numpy as np
import scipy as sc
from scipy import signal


def downsample_by_2(input_value1, input_value2, val=''):
    # Apply low pass filtering by 2 convolve
    print("Calculating downsample by 2")
    print(f"Original values in list: {input_value1}\n{input_value2}")
    if val:
        output_values = np.convolve(input_value1, input_value2, val)
        output_values.round(7)
        print(f"output when val {output_values}")
        return output_values
    else:
        output = np.convolve(input_value1, input_value2)
        print(f"output down sample: {output}")
        return output

def decimate_by_2(output_values, val=None):
    print("Calculating decimate by 2")
    decimation = sc.signal.decimate(output_values, val)
    print(f"Decimation is: {decimation}")
    return decimation
