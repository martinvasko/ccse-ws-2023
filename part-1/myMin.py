def min(*args):
    if len(args) == 1:
        values = args[0]
    else:
        values = args
    if len(values) == 0:
        raise ValueError("myMin() args is an empty sequence")

    for i, value in enumerate(args):
        if i == 0 or value < smallestValue:
            smallestValue = value
    return smallestValue
