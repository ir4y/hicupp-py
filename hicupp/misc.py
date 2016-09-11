def get(array, index, default):
    try:
        return array[index]
    except IndexError:
        return default
