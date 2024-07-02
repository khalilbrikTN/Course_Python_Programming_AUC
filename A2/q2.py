# Student Name : Mohamed Khalil Brik.
# Student ID : 900225905.

# Question 2 : Run-Length Encoding (RLE) algorithm

def rle_encode(text: str) -> str:
    """
    Encodes a string using Run-Length Encoding (RLE).

    Parameters:
    text (str): The input string to be encoded.

    Returns:
    str: The RLE encoded string.
    """
    if len(text) == 0:  # If the input string is empty, return an empty string
        return ''

    rleEncoded = ''  # This will store the encoded string
    counter = 0  # Counter for occurrences of each character
    currentChar = text[0]  # Start with the first character in the string

    for char in text:
        if char == currentChar:  # If the character matches the current character being counted
            counter += 1
        else:  # If a new character is found
            rleEncoded += currentChar + '/' + str(counter) + ' '  # Store the result for the previous character
            currentChar = char  # Change the character being counted
            counter = 1  # Reset counter to 1 for the new character

    rleEncoded += currentChar + '/' + str(counter)  # Add the final character counted

    return rleEncoded

def rle_decode(text: str) -> str:
    """
    Decodes a string that was encoded using Run-Length Encoding (RLE).

    Parameters:
    text (str): The RLE encoded string.

    Returns:
    str: The decoded string.
    """
    if len(text) == 0:  # If the input string is empty, return an empty string
        return ''

    rleDecoded = ''  # This will hold the decoded string
    tokens = text.split(' ')  # Split the encoded string by spaces into tokens

    for token in tokens:
        subToken = token.split('/')  # Split each token by '/' into [char, count]
        char = subToken[0]
        repeat = int(subToken[1])
        string = char * repeat  # Repeat the character 'count' times
        rleDecoded += string  # Add the repeated string to the decoded result

    return rleDecoded


print('__Question 2__')

print('--Test 1--')
text = 'aaabbcccc33335555511'
rleEncoded = rle_encode(text)
rleDecoded = rle_decode(rleEncoded)
print('Original Text:', text)
print('Text RLE Encoded:', rleEncoded)
print('Text RLE Decoded:', rleDecoded)

print('--Test 2--')
text = ''
rleEncoded = rle_encode(text)
rleDecoded = rle_decode(rleEncoded)
print('Original Text:', text)
print('Text RLE Encoded:', rleEncoded)
print('Text RLE Decoded:', rleDecoded)

print('--Test 3--')
text = 'abcde'
rleEncoded = rle_encode(text)
rleDecoded = rle_decode(rleEncoded)
print('Original Text:', text)
print('Text RLE Encoded:', rleEncoded)
print('Text RLE Decoded:', rleDecoded)
