# Name : Mohamed Khalil Brik
# ID : 900225905

from math import *

# Note that we will use a function for each question in this assignment

def q1():
    data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    for index in range(1,len(data)):
        data[index] = data[index-1] + ' plus one'

    # Now we will print the new list after modification
    for index in range(len(data)):
        print(data[index])

    return

def q2():
    string = 'Hello this is a beautiful morning'
    # I will use the replace function which returns a new string without modifying the old one.
    newString = string.replace(' beautiful', '')
    print(newString)

def q3():

    students = [
        ["Alice", "S001", [85, 90, 78]],
        ["Bob", "S002", [80, 88, 92]],
        ["Charlie", "S003", [95, 85, 87]],
        ["David", "S004", [70, 75, 80]],
        ["Eve", "S005", [100, 95, 98]]
    ]

    for row in range(len(students)):
        grades = students[row][-1]
        # grades is a list that has the grades of each student with index row in the matrix of students.
        M = max(grades)
        # M stores the max value of grade for each student with index row.
        m = min(grades)
        # m stores the max value of grade for each student with index row.
        sum = 0 # sum will store the total grades per student, intially equal to 0
        for num in grades:
            sum += num # add each grade to sum

        average = sum/len(grades) # the average is the ratio of the total sum of grades divided by the number of grades.
        students[row].append(average) # append the average to the list of the student
        students[row].append(m) # append the min
        students[row].append(M) # append the max

    # I will now find the student with the maximum grade average.
    Max = 0 # assume the max average is 0
    maxIndex = -1 # this will keep track of the index of the student with the max grade average

    for row in range(len(students)): # row is the index of the current student list
        if(students[row][-3] > Max): #note that the max average of each student is stored at index -3
            Max = students[row][-3]
            maxIndex = row

    print(students)
    print('\n')
    print("Student with Highest Average: " + str(students[maxIndex]))

    return

def q4():
    code = input('Enter postal Code: ')
    # code will store the code entered by the user.

    # check length of the code that must be equal to 7.
    if not (len(code) == 7):
        print('Error : Not Valid Code')
        return # if len is not correct, the code is not valid, so we do not need to check other conditions.

    # check space to be at index 3
    if not (code[3] == ' '):
        print('Error : Not Valid Code')
        return

    # check letters at index 0,2,5 to be upper case alpha letters.
    for index in [0, 2, 5]:
        if not (code[index].isalpha() and code[index].isupper()):
            print('Error : Not Valid Code')
            return

    # check digits at index 1,4,6 to be only digits between 0 and 9
    for index in [1, 4, 6]:
        if not (code[index].isnumeric()):
            print('Error : Not Valid Code')
            return

    # if no error found, the code is correct.
    print('Valid Code')
    return

def q5():
    string = input("Enter you string please: ")

    # we set 4 variables to count each character type : A's, B's, C's and other chars.
    numA = 0
    numB = 0
    numC = 0
    numOther = 0

    for char in string:
        if(char.lower()=='a'): # We will use the lower method to count also upper letters.
            numA += 1
        elif(char.lower()=='b'):
            numB += 1
        elif(char.lower()=='c'):
            numC += 1
        else:
            numOther += 1

    print("Number of A's : " + str(numA))
    print("Number of B's : " + str(numB))
    print("Number of C's : " + str(numC))
    print("Number of other characters : " + str(numOther))

    return


q1()
q2()
q3()
q4()
q5()