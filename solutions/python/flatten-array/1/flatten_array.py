def flatten(iterable):
    result = []
    
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    
    return result