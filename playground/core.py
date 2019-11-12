
def find_peaks(list_of_intensities):
    """Find peaks

    For int and float input: Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.
    For tuple input: Find local minima (darker colors). 
    Intensities are defined as local minima of sum if the
    sum of intensities of the elements in the list before and after 
    are bigger than the peak we want to determine.

    Args:
        list_of_intensities (list of floats, ints or tuples): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    max_value = 0
    list_of_maxima = []
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if type(element) == int:
            if list_of_intensities[pos - 1] < element > list_of_intensities[pos + 1]:
                max_value = element
                list_of_maxima.append(max_value)
        elif type(element) == float:
            if list_of_intensities[pos - 1] < element > list_of_intensities[pos + 1]:
                max_value = element
                list_of_maxima.append(max_value)
        elif type(element) == tuple:
            max_value = (255,255,255)
            if sum(list_of_intensities[pos - 1]) > sum(element) < sum(list_of_intensities[pos + 1]):
                max_value = element
                list_of_maxima.append(max_value)
    return list_of_maxima
