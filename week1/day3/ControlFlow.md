# Day 3 - Control Flow

Control flow is an essential concept in programming that allows you to control the order in which statements and instructions are executed in a program. It enables you to make decisions and repeat certain actions based on conditions. Two fundamental control flow structures in Python are if-else statements and loops.

## If-else statements
If-else statements, also known as conditional statements, are used to perform different actions based on certain conditions. The basic syntax of an if-else statement in Python is as follows:
```
if condition:
    # code to execute if the condition is true
else:
    # code to execute if the condition is false
```
Here, the condition is an expression that evaluates to either True or False. If the condition is True, the code block under the if statement is executed, and if it is False, the code block under the else statement is executed.

Example:

```
age = 30

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
Output:
```
You are an adult.
```

## Loops

Loops allow you to repeat a block of code multiple times. Python supports two types of loops: for loop and while loop.
### For loop
A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. It executes a block of code for each element in the sequence. A basic example of a for loop in Python is as follows:

Example:
```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```
### While loop
A while loop is used to repeatedly execute a block of code as long as a certain condition is True. The condition is evaluated before each iteration. A basic example of a while loop in Python is as follows:

Example:
```
count = 0

while count < 5:
    print(count)
    count += 1
```
Output:
```
0
1
2
3
4
```

In the above example, the while loop continues executing as long as the count is less than 5. Each time the loop iterates, the value of count is incremented by 1.

These are the basic control flow structures in Python that allow you to make decisions with if-else statements and repeat actions with loops. You can combine them to create more complex control flow logic in your programs.