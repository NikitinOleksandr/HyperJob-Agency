import math


# Modify this function in the shell and copy the new version here
def my_sqrt(value):
    if isinstance(value, (float, int)):
        return math.sqrt(value)
    elif isinstance(value, str):
        return "The string should be converted into a numeric data type"
    else:
        return None
