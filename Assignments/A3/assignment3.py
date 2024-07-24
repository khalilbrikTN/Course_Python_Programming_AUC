'''
    Mohamed Khalil Brik -- 900225905
    Notes for users:
        - A line is a sequence of characters ending with the \n character.
        Documentation is added for every function.
'''

#We will define a class of exeptions for this program.

def check_file(name):
    from os import path

    if path.exists(name):
        with open(name, 'r') as file:
            content = file.readlines()
            return content
    else:
        raise FileNotFoundError("The file does not exist. Please check the file name and try again.")
def check_range(value, num_lines):
    if value < 0:
        raise Exception('Negative Line number entered!')
    elif value+1 > num_lines:
        raise Exception('Line number does not exist!')

def replaceLine(fileName, lineNumber, newString):
    """
    Replaces a specific line in a file with a new string.

    Parameters:
    fileName (str): The name of the file.
    lineNumber (int): The line number to be replaced (0-indexed).
    newString (str): The new string to replace the line with.

    Returns:
    None
    """

    # We read the content of the file and check for exceptions.
    content = check_file(fileName)

    l = len(content)

    #Check exceptions for the lineNUmber.
    check_range(lineNumber, l)

    #We modify the lines.
    content[lineNumber] = newString + '\n'

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.writelines(content)
        print("Line number " + str(lineNumber) + " of the file " + fileName + ' has been modified!')

    return

def replaceLines(fileName, lineNumbers, newStrings):
    """
    Replaces multiple specific lines in a file with new strings.

    Parameters:
    fileName (str): The name of the file.
    lineNumbers (list of int): List of line numbers to be replaced (0-indexed).
    newStrings (list of str): List of new strings to replace the lines with.

    Returns:
    None

    Raises:
    Exception: If the sizes of lineNumbers and newStrings do not match.
    """

    # We read the content of the file and check for exceptions.
    content = check_file(fileName)
    l = len(content)

    #We need to check that the len of newStrings is equal to the len of lineNumbers.
    if(len(lineNumbers) != len(newStrings)):
        raise Exception('Sizes of the 2 arrays are not compatible.')

    #Check exceptions for the lineNUmber.
    for index in range(len(lineNumbers)):
        check_range(lineNumbers[index], l)
        content[lineNumbers[index]] = newStrings[index] + '\n'

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.writelines(content)
        print("Line numbers:")
        for number in lineNumbers:
            print(number)
        print(" of the file " + fileName + ' has been modified!')

    return

def deleteLines(fileName, lineNumbers):
    """
    Deletes specific lines from a file by setting them to an empty string.

    Parameters:
    fileName (str): The name of the file.
    lineNumbers (list of int): List of line numbers to be deleted (0-indexed).

    Returns:
    None
    """

    # We read the content of the file and check for exceptions.
    content = check_file(fileName)
    l = len(content)


    #Check exceptions for the lineNumber.
    for index in range(len(lineNumbers)):
        check_range(lineNumbers[index], l)
        content[lineNumbers[index]] = ''

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.writelines(content)
        print("Line numbers:")
        for number in lineNumbers:
            print(number)
        print(" of the file " + fileName + ' has been deleted!')

    return

def swapLines(fileName, lineNumber1, lineNumber2):
    """
    Swaps two specific lines in a file.

    Parameters:
    fileName (str): The name of the file.
    lineNumber1 (int): The first line number to be swapped (0-indexed).
    lineNumber2 (int): The second line number to be swapped (0-indexed).

    Returns:
    None
    """

    # We read the content of the file and check for exceptions.
    content = check_file(fileName)
    l = len(content)


    #Check exceptions for the lineNumber 1 and 2.
    check_range(lineNumber1, l)
    check_range(lineNumber2, l)


    content[lineNumber1], content[lineNumber2] = content[lineNumber2], content[lineNumber1]

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.writelines(content)
        print("Line numbers " + str(lineNumber1) + ' and '+ str(lineNumber2) + ' have been swapped.')
    return

def stripLine(fileName, lineNumber, character):
    """
    Removes all occurrences of a specific character from a specific line in a file.

    Parameters:
    fileName (str): The name of the file.
    lineNumber (int): The line number from which to remove the character (0-indexed).
    character (str): The character to be removed.

    Returns:
    None
    """

    # We read the content of the file and check for exceptions.
    content = check_file(fileName)
    l = len(content)

    check_range(lineNumber, l)

    content[lineNumber] = content[lineNumber].replace(character, '')

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.writelines(content)
        print("Character " + character + ' has been removed from line '+ str(lineNumber) + '.')
    return

def swapCharacters(fileName, charIndex1, charIndex2):
    """
    Swaps two specific characters in a file.

    Parameters:
    fileName (str): The name of the file.
    charIndex1 (int): The index of the first character to be swapped (0-indexed).
    charIndex2 (int): The index of the second character to be swapped (0-indexed).

    Returns:
    None

    Raises:
    Exception: If either index is out of bounds.
    """

    with open(fileName, 'r') as file:
        content = file.read()
    l = len(content)

    if not(0 <= charIndex1 < l and 0 <= charIndex2 < l):
        raise Exception('Index out of bound.')

    char1 = content[charIndex1]
    char2 = content[charIndex2]

    content = content[0:charIndex1] + char2 + content[charIndex1+1:charIndex2] + char1 + content[charIndex2+1::]

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.write(content)
        print("Character at index " + str(charIndex1) + ' and character index '+ str(charIndex2) + ' have been swapped.')
    return
def embed(fileName, startIndex, s):
    """
    Inserts a string into a file at a specific starting index.

    Parameters:
    fileName (str): The name of the file.
    startIndex (int): The starting index where the string will be inserted (0-indexed).
    s (str): The string to be inserted.

    Returns:
    None

    Raises:
    Exception: If the startIndex is out of bounds.
    """

    with open(fileName, 'r') as file:
        content = file.read()
    l = len(content)

    if not(0 <= startIndex < l):
        raise Exception('Index out of bound.')

    content = content[0:startIndex] + s + content[startIndex+1::]

    #We write to the file the new lines.
    with open(fileName, 'w') as file:
        file.write(content)
        print("String " + s + ' has been inserted at index '+ str(startIndex) + '.')
    return




#Test the functions.

#replaceline.
replaceLine('text.txt', 1,'hi')

#replaceline.
replaceLines('text.txt', [1,2],['a', 'b'])

#deletelines
replaceLines('text.txt', [1,2],['a', 'b'])

#swapLines
swapLines('text.txt', 2,3)

#stripline
stripLine('text.txt', 4, 'o')

#swapCharacters
swapCharacters('text.txt',2,3)

#embed
embed('text.txt', 6, 'this line is added.')

