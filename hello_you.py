# Ask user for name

name = input ("What is your name?: ")
print (name)

# Ask user for age

age = input ("How old are you?: ")
print(name)
print(age)

# Ask user for city

city = input ("Which is your city?: ")
print (city)


# Ask user what they enjoy

love = input ("What do you enjoy?: ")
print (love)


# Create output text

string = "Your name is {}, you are {} years old. You live in {} and you love {}."
output = string.format (name,age,city,love)


# Print output to screen 

print (output)

