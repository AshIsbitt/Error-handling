try:
    file = open("order.txt", "r")
except FileNotFoundError as err:
    print("File doesn't exist")
    print(err)
    #raise forces the red-text error to happen. If this was in a while true loop, the above text would print out
    # infiniately without this
    raise