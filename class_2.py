def roman_to_integer(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

# Accept user input
roman_input = input("Enter a Roman numeral: ").upper()

# Convert and display the result
try:
    integer_result = roman_to_integer(roman_input)
    print(f"The integer equivalent of {roman_input} is: {integer_result}")
except KeyError:
    print("Invalid Roman numeral input.")
