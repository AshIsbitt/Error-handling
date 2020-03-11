# Open and read

def open_and_print(file_name):
    try:
        with open(file_name, 'r') as file:
            lines_list = file.readlines()
            for line in lines_list:
                print(line.strip("\n"))

    except FileNotFoundError as err:
        print("Check files")
        print(err)

    finally:
        print("Closing program")

# Open and write

def open_and_write(file_name, new_text):

    try:
        with open(file_name, 'w') as file_to_write:
            file_to_write.write(new_text)
    except FileNotFoundError as err:
        print("Check files")
        print(err)

    finally:
        print("Closing program")
