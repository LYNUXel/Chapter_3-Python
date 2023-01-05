n = int(input("Number: "))

# EXCEPTION => TypeError: '>' not supported between instances of 'str' and 'int'
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
