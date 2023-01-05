# Is an function that takes an other function as input and return a modified version of that function as an output
def announce(f):
    def wrapper():
        print("About the function...")
        f()
        print("Done with with the function.")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()