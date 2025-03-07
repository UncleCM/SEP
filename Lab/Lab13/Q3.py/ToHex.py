class InvalidArgument(Exception):
    pass

def toHex(n):
    if not isinstance(n, int) or n <= 0:
        raise InvalidArgument("Input must be a positive integer")
    return hex(n)[2:].upper()

def fromHex(n):
    if not isinstance(n, str) or not n.isalnum():
        raise InvalidArgument("Input must be a hexadecimal string")
    return int(n, 16)

# print(toHex(14))  # Output: "E"
# print(toHex(171)) # Output: "AB"
# def main():
#     try:
#         n = int(input("Enter a positive integer: "))
#         print(toHex(n))
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#     except InvalidArgument as e:
#         print(e)

