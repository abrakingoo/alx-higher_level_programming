#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:

        return 0

    else:
        mapping = {

                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }

        length_of_input = len(roman_string)

        i = length_of_input - 1

        output = 0

        while i >= 0:

            if i < length_of_input - 1 and \
                mapping[roman_string[i]] < \
                    mapping[roman_string[i + 1]]:

                output -= mapping[roman_string[i]]

            else:
                output += mapping[roman_string[i]]

            i -= 1

        return output
