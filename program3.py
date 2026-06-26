num = int(input("Enter a number: "))
text = input("Enter a string: ")

if num >= 10 and num <= 20:
    print("Number is within range")
else:
    print("Number is not within range")

if text == "python" or text == "Python":
    print("String matched")
else:
    print("String not matched")

# Output:
# Enter a number: 15
# Enter a string: Python
# Number is within range
# String matched
