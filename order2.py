# try:
#     file = open("order.txt", "r")
# except FileNotFoundError as err:
#     print("File doesn't exist")
#     print(err)
#     #raise forces the red-text error to happen. If this was in a while true loop, the above text would print out
#     # infiniately without this
#     raise

try:
    with open("order.txt", 'r') as file:
        lines_list = file.readlines()
        for line in lines_list:
            print(line.strip("\n"))

except FileNotFoundError as err:
    print("Check files")
    print(err)

finally:
    print("Closing program")