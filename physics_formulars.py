def area_of_circle():
    r = float(input("Enter radius:"))
    area = 3.14159 * r * r
    print("Area of circle =", area)

def speed():
    d = float(input("Enter distance:"))
    t = float(input("Enter time:"))
    speed = d / t
    print("Speed =", speed)

def volume_of_a_cube():
    l = float(input("Enter the lenght:"))
    volume = l * l * l
    print("Volume of a cube =", volume)

def simple_interest():
    p = float(input("Enter Principal:"))
    r = float(input("Enter Rate:"))
    t = float(input("Enter Time:"))
    si = (p * r * t) / 100
    print("Simple Interest =", si)

def density():
    m = float(input("Enter Mass:"))
    v = float(input("Enter Volume:"))
    density = m / v
    print("Density =", density)

def acceleration():
    v = float(input("Enter the Volume:"))
    t = float(input("Enter the Time:"))
    acceleration = v / t
    print("Acceleration =", acceleration)

while True:
    print("1. Area of a Circle")
    print("2. Speed")
    print("3. Volume of a Cube")
    print("4. Simple Interest")
    print("5. Density")
    print("6. Acceleration")

    choice = input("Pick a formula (1–6): ")

    if choice == "1":
        area_of_circle()
    elif choice == "2":
        speed()
    elif choice == "3":
       volume_of_a_cube()
    elif choice == "4":
        simple_interest()
    elif choice == "5":
        density()
    elif choice == "6":
       acceleration()
    else:
        print("Try again.")