def get_or_default(items, index=0, default=None):
    """
    :param items: List or Tuple or Array
    :param index: Desired index to search
    :param default: Default Value in case of none or IndexError
    :return: Item at the given index on a list, or default value in case if doesn't exist
    """
    if items is None:
        return default

    try:
        return items[index] or default
    except IndexError:
        return default
