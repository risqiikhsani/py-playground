def my_function(parameter1, parameter2):
    # Function body
    result = parameter1 + parameter2
    return result

output = my_function(1, 2)
print(output)



# 1. *args (Non-Keyword Variable-Length Arguments):

#     Used to pass a variable number of non-keyword arguments to a function.
#     The asterisk * before args indicates that any number of positional arguments can be passed to the function.
#     Inside the function, args is treated as a tuple containing all the positional arguments passed during the function call.

def test_args(*args):
    for arg in args:
        print(arg)

test_args(1, 2, 3)  # Output: 1 2 3
test_args('a', 'b', 'c', 'd')  # Output: a b c d


# 2. **kwargs (Keyword Variable-Length Arguments):

#     Used to pass a variable number of keyword arguments (key-value pairs) to a function.
#     The double asterisk ** before kwargs indicates that any number of keyword arguments can be passed to the function.
#     Inside the function, kwargs is treated as a dictionary containing all the keyword arguments passed during the function call.

def test_kwargs(**kwargs):
    for k,i in kwargs.items():
        print(f"{k}:{i}")

test_kwargs(name="John", age=30)  # Output: name:John age:30
test_kwargs(country="USA", city="New York")  # Output: country:USA city:New York



# Regular function
def add(x, y):
    return x + y

print(add(2, 3))  # Output: 5

# Equivalent lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))  # Output: 5
