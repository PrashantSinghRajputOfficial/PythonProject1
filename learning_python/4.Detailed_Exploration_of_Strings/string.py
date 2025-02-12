# Detailed Exploration of Strings

# geting input string

paraghrap = input("write a paraghrap: ")

print("\nAap ne ho paradhrap likha vo ye hai :", paraghrap)

# string manipulation

# The .upper() string method converts all characters of a string into capital letters.

print("\nAll characters of paraghrap into capital letters:",paraghrap.upper())

# The .lower string method convert all characters of a string into small letters.

print("\nAll characters of paraghrap into small letters:",paraghrap.lower())

# The .split() string method splits a string into words based on spaces.

print("\nSplits praraghrap into words:",paraghrap.split())

# String Concatenation:

concatenated_string = "your paraghrap: " + paraghrap + " it is correct"
print("\nConcatenated string:")
print(concatenated_string)

#5. String Slicing:

if len(paraghrap) > 10:
    sliced_string = paraghrap[:10]  # Pehle 10 characters
else:
    sliced_string = paraghrap         # Poora string agar length 10 se kam hai
print("\nSliced string (pehle 10 characters):")
print(sliced_string)

# Formatting using f-string:

print(f"your paraghrap is: ",paraghrap," correct")

# formatting using .format() method:

formatted_output2 = "your parafhrap is : '{}' correct".format(paraghrap)
print("\nFormatted output using format() method:")
print(formatted_output2)

