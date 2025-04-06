#validating password
import re

password_pattern =  r"\b(?=\S{8,})(?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)(?=\S*[@#$%^&+=!])\S+\b"
text = "Your password is Welcome@123"
match = re.search(password_pattern, text)
if match:
    print("Valid password found:", match.group())
else:
    print("No valid password found.")



#validating url

url_pattern = r"(https?://|www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?"

text = "Visit our website at https://www.example.com/about"
match = re.search(url_pattern, text)
if match:
    print("Valid URL found:", match.group())
else:
    print("No valid URL found.")


# implementing all errors using exception handling

try:
    num = int(input("Enter a number: "))

    # ZeroDivisionError
    result = 10 / num

    # TypeError
    print("Result:",result)     # o/p - if we give number : Cannot divide by zero.
                                # if we give string : Invalid input: invalid literal for int() with base 10: 're'
    # IndexError
    my_list = [1, 2, 3]
    print("Accessing index 5:", my_list[5])     # o/p - Index out of range: list index out of range

    # KeyError
    my_dict = {"name": "Navya"}
    print("Accessing age:", my_dict["age"])     # o/p - Key not found in dictionary: 'age'

    # FileNotFoundError
    with open("missing_file.txt", "r") as file:
        data = file.read()          # o/p - File not found: [Errno 2] No such file or directory: 'missing_file.txt' 

except ValueError as e:
    print("Invalid input:", e)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except TypeError as e:
    print("Type error occurred:", e)

except IndexError as e:
    print("Index out of range:", e)

except KeyError as e:
    print("Key not found in dictionary:", e)

except FileNotFoundError as e:
    print("File not found:", e)

except Exception as e:
    print("Unexpected error:", e)

else:
    print("Result:", result)

finally:
    print("Code executed successfully.")
