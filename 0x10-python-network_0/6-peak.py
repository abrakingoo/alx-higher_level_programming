#!/usr/bin/python3
"""
 a function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """
     a function that finds a peak in a list of unsorted integers.
    """

    if not list_of_integers:
        return None

    # Check for positive peaks
    positive_peaks = [num for num in list_of_integers if num >= 0]

    if positive_peaks:
        return max(positive_peaks)

    # If no positive peaks found, find the highest peak (including negative ones)
    return max(list_of_integers)

