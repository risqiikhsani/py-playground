
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Creating a list
my_list = ["apple", "banana", "cherry"]

# Accessing elements of the list
print(my_list[0])  # Output: apple

# Modifying elements of the list
my_list[1] = "orange"
print(my_list)  # Output: ['apple', 'orange', 'cherry']

# Adding elements to the list
my_list.append("banana")
print(my_list)  # Output: ['apple', 'orange', 'cherry', 'banana']

# Removing elements from the list
my_list.remove("orange")
print(my_list)  # Output: ['apple', 'cherry', 'banana']


# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing elements of the tuple
print(my_tuple[0])  # Output: apple

# Tuple is unchangeable, so attempting to modify it will raise an error
# my_tuple[1] = "orange"  # Raises TypeError


# Creating a set
my_set = {"apple", "banana", "cherry"}

# Adding elements to the set
my_set.add("orange")
print(my_set)  # Output: {'apple', 'banana', 'orange', 'cherry'}

# Removing elements from the set
my_set.remove("banana")
print(my_set)  # Output: {'apple', 'orange', 'cherry'}


# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing values in the dictionary
print(my_dict["name"])  # Output: John

# Modifying values in the dictionary
my_dict["age"] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Adding new key-value pairs to the dictionary
my_dict["gender"] = "Male"
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'gender': 'Male'}

# Removing key-value pairs from the dictionary
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'gender': 'Male'}
