color = ["red", "green"]
things = ["T-shirt", "skirt"]

for x in color :
    print("outer loop ",x)
    for y in things :
        print("***inner loop*** ", y)
        print(x,y)
    print("")