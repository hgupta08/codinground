def int_to_str(num):
    if num == 0:
        return '0'

    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    result = ''
    while num > 0:
        result = chr((num % 10) + ord('0')) + result
        num = num // 10

    if is_negative:
        result = '-' + result

    return result

# Example usage:
number = 12345
string_representation = int_to_str(number)
print(f"The string representation of {number} is '{string_representation}'")