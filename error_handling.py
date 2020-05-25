num = input("Enter a number: ")
try:
    num **2
except TypeError:
    print("Two or more type do not agree")
finally:
    print(f"The number collected was {num}")
    print("this is the last line")
