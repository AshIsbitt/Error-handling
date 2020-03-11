
#This opens a file... except it throws an error up because this doesn't exist
# file = open('order.txt')

try:
    file = open('order.txt', 'r')
    file_line_list = file.readlines()

    print(file_line_list)

    for line in file_line_list:
        #This line will also remove the \n on the end of each item.
        print(line.rstrip("\n"))

    file.close()
    
except FileNotFoundError as errmsg:
    print("THERE HAS BEEN AN ERROR")
    print(errmsg)