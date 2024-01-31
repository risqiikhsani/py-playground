# Python does not have built-in support for Arrays, but Python Lists can be used instead.


# This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.


# using list as arrays

# Creating a list to represent an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements of the array
print(my_array[0])  # Output: 1

# Modifying elements of the array
my_array[1] = 10
print(my_array)  # Output: [1, 10, 3, 4, 5]

# Adding elements to the array
my_array.append(6)
print(my_array)  # Output: [1, 10, 3, 4, 5, 6]

# Removing elements from the array
my_array.remove(3)
print(my_array)  # Output: [1, 10, 4, 5, 6]


# using numpy

import numpy as np

# Creating a NumPy array
my_array_np = np.array([1, 2, 3, 4, 5])

# Accessing elements of the array
print(my_array_np[0])  # Output: 1

# Modifying elements of the array
my_array_np[1] = 10
print(my_array_np)  # Output: [ 1 10  3  4  5]

# Adding elements to the array
# NumPy arrays have a fixed size, so you can't directly add elements.
# Instead, you create a new array with the desired elements.
my_array_np = np.append(my_array_np, 6)
print(my_array_np)  # Output: [ 1 10  3  4  5  6]

# Removing elements from the array
# NumPy arrays don't have a built-in method to remove elements.
# Instead, you create a new array without the desired elements.
my_array_np = my_array_np[my_array_np != 3]
print(my_array_np)  # Output: [ 1 10  4  5  6]
