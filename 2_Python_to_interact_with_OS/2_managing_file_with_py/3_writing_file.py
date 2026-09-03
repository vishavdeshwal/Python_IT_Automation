
# By default open function uses the "r" mode, which is read only
# To enable writing, we need to use the "w" mode.

# The "a" mode is append mode -------> Appending anything at the end of the content of file
# The "r+" mode is read and write mode -------> Reading and writing at the same time
# The "w" mode is write mode -------> Writing anything in the file but cannot read from it. It will also overwrite your content and not append anything.
# The "x" mode is exclusive creation mode -------> Creating a file but cannot read from it
# The "b" mode is binary mode -------> Reading and writing in binary format
# The "t" mode is text mode -------> Reading and writing in text format
with open('spider.txt', 'a') as file:
    file.write("It was a dark and stormy night1.\n")
    


# ------------------------------------------------

# with open('guests.txt') as guests:
#     for line in guests:
#         print(line)

new_guests = ['Alice', 'Bob', 'Charlie', 'Dave']

# with open('guests.txt', 'a') as guests:
#     for guest in new_guests:
#         guests.write(guest + '\n')
# guests.close()


with open('guests.txt') as guests:
    for line in guests:
        print(line)




