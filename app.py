print("Hello World 😊")
# Strings usage
# If you want to write a long sentence, you can use triple quotes
long_sentence = """This is a long sentence that spans multiple lines."""
print(len(long_sentence))
# slice in python is pretty straightforward usiing the colon operator
# string[start:end] where start is inclusive and end is exclusive
print(long_sentence[0:10])  # prints first 10 characters
print(long_sentence[0:])  # prints the whole new string
print(long_sentence[:10])  # prints first 10 characters


# if you want to trim and remove whitespace from both ends of a string, you can use the strip() method
trimmed_string = "   Hello, World!   "
print(trimmed_string.strip())  # prints "Hello, World!"
# you can also use lstrip() and rstrip() to remove whitespace from the left and right ends respectively
print(trimmed_string.lstrip())  # prints "Hello, World!   "
# To make the first letter of each word uppercase, you can use the title() method
title_string = "hello world from python"
print(title_string.title())  # prints "Hello World From Python"
# To convert a string to uppercase, you can use the upper() method

# If you want to get the index of a substring within a string, you can use the find() method
index = long_sentence.find("long")  
print(index)  # prints the index of the first occurrence of "long"

# If we want to replace a substring with another substring, we can use the replace() method
replaced_string = long_sentence.replace("long", "short")
print(replaced_string)  # prints the string with "long" replaced by "short"

temperature = 25
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day") 
print("Goodbye! 👋")


age = 22
# if age >= 18:
#     message = "You are an adult."
# else:
#     message = "You are a minor."
message = "You are an Adult." if age >= 18 else "You are a minor."
print(message)

# Looping through a list
fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
    print(fruit)
# Looping through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")