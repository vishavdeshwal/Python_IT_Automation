file = open('spider.txt')

# With this file object, we can read and perform different operations on the file.


# It will only read the first line of the content from the file
print(file.readline())


# It will read the entire content of the file
print(file.read())


# This will close the file just like you close it when you open any file.
file.close()



# So to prevent closing file after every operation, python has with keyword

with open('spider.txt') as file:
    print(file.readline())

# This will automatically close the file after the operation is done.


# -------------------------------------------
