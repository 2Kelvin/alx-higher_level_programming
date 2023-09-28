"""Find a peak module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted ints"""
    for n in range(len(list_of_integers)):
        if len(list_of_integers) == 0:
            return None
        if list_of_integers[n] > list_of_integers[n + 1]:
            return n
    return len(list_of_integers) - 1
