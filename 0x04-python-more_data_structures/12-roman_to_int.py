#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    number = 0
    string = roman_string + ' '
    for i in range(len(string)):
        if string[i] == 'I':
            if string[i + 1] == 'V' or string[i + 1] == 'X':
                number -= 1
            else:
                number += 1
        elif string[i] == 'V':
            number += 5
        elif string[i] == 'X':
            if string[i + 1] == 'L' or string[i + 1] == 'C':
                number -= 10
            else:
                number += 10
        elif string[i] == 'L':
            number += 50
        elif string[i] == 'C':
            if string[i + 1] == 'D' or string[i + 1] == 'M':
                number -= 100
            else:
                number += 100
        elif string[i] == 'D':
            number += 500
        elif string[i] == 'M':
            number += 1000
    return number
