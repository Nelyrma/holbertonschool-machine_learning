#!/usr/bin/env python3
"""function that concatenates two arrays element-wise"""

def cat_arrays(arr1, arr2):
    """concatenates two arrays

    Args:
        arr1 : the first array
        arr2 : the second array

    Returns:
        a new array
    """
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    
    concat_array = []
    
    for i in range(len_arr1):
        concat_array.append(arr1[i])
    for j in range(len_arr2):
        concat_array.append(arr2[j])
        
    return concat_array
