print("hello babe")
#has automatic type conversion and also lets us explicit conversion
a=100
b=1.2
"""
print(type(a))
print(type(b))

print(ord('A'))  # Output: 65

print(chr(65))  # Output: 'A'
"""

#and or not in not in is is not

x,y = input("Enter Name and age").split(",")

print(f"Name is {x} and age is {y}")

if condition1:
    # Execute this block if condition1 is True
elif condition2:
    # Execute this block if condition2 is True
elif condition3:
    # Execute this block if condition3 is True
else:
    # Execute this block if none of the above conditions are True

s = "Hello, World!"

print(s[2:5])  # Output: "llo"
print(s[:])  # Output: "Hello, World!"
print(s[:5])  # Output: "Hello"
# string[start:end:step]: Extracts with a specified step 
print(s[::2])  # Output: "Hoo ol!"
#skips every 2 chars
print(s[::-1])  # Output: "!dlroW ,olleH"
#The -1 step reverses the string.

{"item_id": item_id, **item_dict} : ** merging key values like spread operator from js