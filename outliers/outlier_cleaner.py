#!/usr/bin/python

import math
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    temp_data = []

    try:
        for i in range(len(predictions)):
            difference = math.pow(abs(predictions[i] - net_worths[i]), 2)
            temp_data.append((ages[i], net_worths[i], difference))
            # print predictions[i], net_worths[i], "difference - ", math.pow(abs(predictions[i] - net_worths[i]), 2)
    except Exception as e:
        print e

    cleaned_data = sorted(temp_data, key = lambda x: x[2])

    ninety_percent_data = int(round(len(predictions) * 0.9))
    print ninety_percent_data

    cleaned_data = cleaned_data[:ninety_percent_data]

    # print cleaned_data

    return cleaned_data

