#!/usr/bin/python


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
    for x in range(0, len(predictions)):
        predictions[x] = abs(predictions[x] - net_worths[x])
    for y in range(0, 9):
        maxim = 0
        index = -1
        for x in range(0, len(predictions)):
            if predictions[x] > maxim:
                maxim = predictions[x]
                index = x
        ages[index] = -1
        net_worths[index] = -1
        predictions[index] = -1
    for x in range(0, len(predictions)):
        if (predictions[x] > -1):
            cleaned_data.append(tuple((ages[x], net_worths[x], predictions[x])))
    return cleaned_data

