def introduction(name, greeting="Hello"):
    print(f"{greeting} {name}")


introduction("Martin")
introduction("Martin", "Good morning")


def simple(*args):
    for arg in args:
        print(f"Argument: {arg}")


simple("first", "second", "third")
myList = ["dog", "cat", "fish"]
simple(*myList)


def mapping(**args):
    for key in args:
        print(f"{key}: {args.get(key)}")


myMap = {"1": "first"}
mapping(**myMap)
