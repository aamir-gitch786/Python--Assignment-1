'''2. Develop a Python program to find volume and surface area of cuboid.
Hint:-
v=l*b*h
sa=2*(l*b+b*h+h*l)'''

l = float(input("Enter length "))
b = float(input("Enter breadth"))
h = float(input("Enter height"))

print(f"Volume of cuboid is {l*b*h} \nSurface area of cuboid is {2*(l*b+b*h+h*l)}")