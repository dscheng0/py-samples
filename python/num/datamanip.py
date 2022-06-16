def flatten_array(nested_array):
    """
    Flatten an array of arbitrarily nested arrays of integers
    into a flat array of integers

    :Args:
    nested_array (iterable of ints): potentially nested array of ints

    :Return:
    (list) flat array of ints

    :Raises:
    ValueError if non list or int values found
    """
    flat_array = []
    for item in nested_array:
        if type( item ) is list:
            flat_array.extend( flatten_array( item ) )
        elif type( item ) is int:
            flat_array.append( item )
        else:
            raise ValueError("Unexpected value in array")
    return flat_array
