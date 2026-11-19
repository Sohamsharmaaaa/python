# Write a function parse_port(value) that takes a string from user input and returns it as an integer port number. If the string is not a valid integer, catch the ValueError and print "Invalid port: not a number". If the number is outside the range 1-65535, raise a exception with a meaningful message and handle it in the caller. Use a finally block to print "Validation complete" regardless of the outcome.


def parse_port(value):
    try:
        port = int(value)
    except ValueError:
        raise ValueError("Invalid port: NOt a number")
    if port < 1 or port > 65535:
        raise Exception("Port number must be between 1 and 65535")
    return port


try:
    port = input("Enter port number: ")
    result = parse_port(port)
    print("Valid port number: ", result)
except ValueError as e:
    print(e)
finally:
    print("Validation complete")
