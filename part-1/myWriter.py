try:
    with open("sample.txt", "w") as fileObj:
        fileObj.write("Hello, world!")
        eggs = 42 / 0
except:
    print("Some error happened!")
