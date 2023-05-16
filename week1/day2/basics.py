name = "Iman"
is_working_hier = True
heigh_in_meter = 1.81
age = 30


print("name:", name )
print("does", name,  "works hier:", is_working_hier)
print(name, "'s height: ", heigh_in_meter)
# a better method to print more complex sentence
print(f"{name}'s age: {age}")


name = input("Enter your name:")
# cast to int 
age = int(input("Enter your age:"))
# cast to float
height = float(input("Enter your height in meter:"))
# cast to boolean
is_working = bool(input("Do you have work (if the answer is No Just enter):"))

print(f"Hello {name} you are {age} years old, your height is {height} and, your working status is {is_working}")
