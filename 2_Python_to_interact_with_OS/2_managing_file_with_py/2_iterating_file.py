

with open('spider.txt') as file:
    for line in file:
        print(line.upper())



# The strip() method removes any leading and trailing whitespace characters (space, tab, newline).
# The upper() method converts the string to uppercase.
with open('spider.txt') as file:
    for line in file:
        print(line.strip().upper())




# # The readlines() method reads all the lines in a file and returns them as a list.
# The sort() method sorts the list in ascending order.
# The sort() method is case-sensitive, so it will sort uppercase letters first.
file = open('spider.txt')
lines = file.readlines()
print(lines)
file.close()

lines.sort()
print(lines)
