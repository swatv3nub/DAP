import math

def area_of_circle(radius):
    area = math.pi * radius**2
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle_area = area_of_circle(radius)
    print("The area of the circle is:", circle_area)
if __name__ == '__main__':
    main()
