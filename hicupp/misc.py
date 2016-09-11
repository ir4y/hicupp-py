def get(array, index, default):
    try:
        return array[index]
    except IndexError:
        return default


def is_sequence(arg):
    return (not isinstance(arg, str) and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))
