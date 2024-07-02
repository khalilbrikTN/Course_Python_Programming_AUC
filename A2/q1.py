# Student Name : Mohamed Khalil Brik.
# Student ID : 900225905.

# Question 1 : all possible permutations of integer values in [0,x] and [0,y].

def q1(x: int, y: int):
    """
    Accept two integers from the user (x and y). Generate and print all possible
    permutations of integer values in [0,x] and [0,y].

    Parameters:
    x (int): The upper limit for the first range (inclusive).
    y (int): The upper limit for the second range (inclusive).

    Returns:
    List[List[int]]: A list of lists, where each inner list contains a permutation
                     of an integer from [0, x] paired with an integer from [0, y].
    """
    arrayX = list(range(x + 1))  # Generates a list of numbers from 0 to x (inclusive)
    arrayY = list(range(y + 1))  # Generates a list of numbers from 0 to y (inclusive)

    permutations = []  # Will store all possible permutations from both lists
    for num1 in arrayX:  # Iterate through each number in arrayX
        for num2 in arrayY:  # Iterate through each number in arrayY
            permutations.append([num1, num2])  # Add each combination to the permutations list
    return permutations

print('__Question 1__')

x, y = 2, 3
print('--Test 1--')
print('x =', x)
print('y =', y)
print('Permutations:', q1(x, y))

x, y = 5, 7
print('--Test 2--')
print('x =', x)
print('y =', y)
print('Permutations:', q1(x, y))

x, y = 1, 4
print('--Test 3--')
print('x =', x)
print('y =', y)
print('Permutations:', q1(x, y))
