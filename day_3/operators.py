age = int
height = float
complex = (1 + 1j)

# area of a triangle for lenght of 0.5
base = int(input("Enter base: "))
height = int(input("Enter height: "))
lenght = 0.5
area_of_triangle = base * height * lenght
print("The area of the triangle is ", area_of_triangle)

# area of a triangle
side_a = int(input("Enter side a: ")) 
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimeter = side_a + side_b + side_c 

print("The perimeter of a triangle is: ", perimeter)

# area of a rectangle
length = int(input("Enter lenght: "))
width = int(input("Enter width: "))

area = lenght * width
perimeter_of_rectangle = 2 * lenght + width
print("The area of a rectangle is: ", area)
print("The perimeter of a rectangle is :", perimeter_of_rectangle)

# area and circumference
radius = int(input("enter radius: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is: ", area, "and the circumference is: ", circumference)

# slope
m = 2

#
first_word = "python"
second_word = "dragon"

print(len(first_word) == len(second_word))
print(len("mango") != len("avocado"))
print(len("mango") != len("avocado"))
print("jargon" in "I hope this course is not full of jargon")
print("on" in "dragon:", "on" in "python")

word = "python"
word_lenght = len(word)

print(float(word_lenght))
print(str(word_lenght))

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour

print(f"Your weekly earning is: {weekly_earning}")

number_of_years = int(input("Enter number of years: "))
number_of_seconds = number_of_years * 60 * 60 * 24 * 365

print(f"You have lived for {number_of_seconds} seconds")

for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)
