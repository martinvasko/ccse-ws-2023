def callItTwice(func, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)
