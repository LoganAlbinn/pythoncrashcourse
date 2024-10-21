# variables are one of the most essential parts of any programming language.
# a variable holds a value, then instead of using that value, the variable can be used to represent it.
# a variable declaration involves writing the variable name on the left, equals sign in the middle, and the value on the right
1 = "y"
x = "Hello"
y = "World"

print(x,y,z)

# as you can see the x and y are the variable names, neither of which are surrounded by parenthesis. However, the value on the right does have parenthesis.

# Run the script and see what happens.

# It printed Hello World

# try adding a new variable z. Make sure you declare z above the print statement
# Then change the print to print(x,y,z)
# What prints out? # It printed Hello World Ironman
# What if we declare a variable from another variable? What if you write:
# x = "Hello"
# y = "World"
# z = y
# print(x,y,z)
# What prints now? Hello World y

# You should see "Hello World World". This is because a variable can also be assigned from another variable! Notice that, in this case the y didn't have quotation marks around it even though it was on the right side.

# What happens if we don't use quotation marks? NameError: name 'hello' not identified
# x = "Hello"
# y = "World"
# z = "y"
# print(x,y,z)
# What prints now?

# You should see "Hello World y". This is because the y is not actually the variable y, but instead just the value of y. You'll see more about this in the next section.

# BREAK IT:
# What happens if you try to use a number as a variable name? I get SyntaxError: cannot assign to literal here. And it suggest a correction.
# For example: 
# 1 = "Hello"
# Why do you think the error occurs? I think this error occurs because I am missing the proper syntax for python to recognize my variable name. It's like trying to use a target gift card at best buy, it just doesn't work.