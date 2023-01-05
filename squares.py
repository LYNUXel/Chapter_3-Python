# importing functions from other python modules or files

from functions import square

for i in range(10):
    print(f"The i square of {i} is {square(i)}")


# or
import functions

for j in range(10):
    print(f"The j square of {j} is {functions.square(j)}")