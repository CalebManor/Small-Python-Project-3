# Caleb Manor

# PROGRAM THREE - comp3100p3.py
# Create a string variable and store the word "Harding University"
# Print out the string in all lower case using a string method (research)
# Print out the string in reverse using a loop and output all on one line
# Print out the following: "The string HARDING UNIVERSITY has 18 characters

a_string = "Harding University"
reverse_string = a_string[::-1]

output_text = "The string {} has {} characters"
str_len = len(a_string)

print(a_string.lower())
for i in reversed(a_string):
    print(i, end="")
print()
print(output_text.format(a_string, str_len))