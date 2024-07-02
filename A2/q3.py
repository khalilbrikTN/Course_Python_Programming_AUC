# Student Name : Mohamed Khalil Brik.
# Student ID : 900225905.

# Question 3 : Stem and Leaf Plot
def stemLeafPlot(data):
    """
    Generates a stem and leaf plot from a list of integers.

    Parameters:
    data (list): A list of integers to be used for generating the stem and leaf plot.

    Returns:
    list: A sorted list of tuples, where each tuple contains a stem and a sorted list of leaves.
    """
    table = {}  # Dictionary to keep track of stems and their corresponding leaves.

    for num in data:  # Iterate through each number in the data list.
        leaf = int(str(num)[-1])  # Extract the last digit as the leaf.
        stem = int(str(num)[:-1])  # Extract the remaining digits as the stem.
        if stem in table:  # If the stem is already in the table,
            table[stem].append(leaf)  # append the leaf to the existing list of leaves.
        else:  # If the stem is not in the table,
            table[stem] = [leaf]  # create a new entry with the stem and the leaf.

    # Convert the dictionary to a sorted list of tuples based on the stem.
    table = sorted(table.items(), key=lambda table: table[0])
    for index in range(len(table)):
        table[index][1].sort()  # Sort the list of leaves for each stem.

    return table

print('__Question 3__')

data = [112, 72, 69, 97, 107, 73, 92, 76, 86, 73,
        126, 128, 118, 127, 124, 82, 104, 132, 134, 83,
        92, 108, 96, 100, 92, 115, 76, 91, 102, 81,
        95, 141, 81, 80, 106, 84, 106, 119, 113, 98, 75,
        68, 98, 115, 106, 95, 100, 85, 94, 106, 119]

table = stemLeafPlot(data)

print('data:', table)
print('Stem and Leaf Diagram:')
for row in table:
    print(row)
