import math

# Define some functions for logarithms and exponents
def eval_safe(expression):
    # Create a safe environment with allowed functions
    safe_dict = {
        'log': math.log,  # natural log (base e)
        'log10': math.log10,  # log base 10
        'pow': math.pow,  # exponentiation function
        'sqrt': math.sqrt,  # square root function
        'exp': math.exp,  # exponent function e^x
        'pi': math.pi,  # constant pi
        'e': math.e  # constant e
    }
    
    # Evaluate the input string in a safe environment
    return eval(expression, {"__builtins__": None}, safe_dict)

# String expression containing logarithms and exponents
expression = input("Enter the expression (logarithms and exponents): ")
print(type(expression))

try:
    # Calculate the result
    result = eval_safe(expression)
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
