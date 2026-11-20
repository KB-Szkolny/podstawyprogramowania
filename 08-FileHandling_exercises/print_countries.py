###
# Reads from file, line by line
#
with open('1-Reading_from_File/countries.txt', 'r') as file:
    for line in file:
        print(line, end="")