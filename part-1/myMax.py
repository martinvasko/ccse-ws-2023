def max(**args):
    biggestValue = {"default": 0}
    for key in args.keys():
        print(f"{key} : {args.get(key)}")
