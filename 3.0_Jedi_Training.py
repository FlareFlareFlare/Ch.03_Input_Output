# Sign your name: Matthew FLYR
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("What is your name?")
print(name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = int(input("What is the base? :"))
height = int(input("What is the height? :"))
area = (base * height) / 2
print(area)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float(input("What is the radius? :"))
circum = 2*3.14*radius
print(circum)

# 4. Ask a user for an integer and then print the square root.
num = int(input("Pick a number, any number... :"))
sqaurey = num**.5
print(sqaurey)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
print("A good star wars joke is May the mass times acceleration be with you, because F=ma")
mass = int(input("What is the mass? : "))
accel = int(input("What is the acceleration? : "))
force = mass*accel
print(force)
print("Get it?!?!?!?!?!?!?!?!")


