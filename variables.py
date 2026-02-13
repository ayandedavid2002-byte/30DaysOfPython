# Day 2: 30 Days of python programming
first_name = "David" 
last_name = "Ayande"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Makurdi"
age = 23
year = 2026
is_married = "single"
is_true, is_light_on = "yes" , "yes"


print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

num_one, num_two = 5 , 4

variable_total = num_one + num_two
variable_diff = num_one - num_two
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainder = num_one % num_one
variable_exp = num_one ** num_two
floor_division = num_one // num_two

#radius_of_a_circle = 30
def area_of_circle(r):
    result = (3.14 * radius * radius)
    return result
radius = 30
result = area_of_circle(radius)
print(result)

first_name = input("put your first name: ")
last_name = input("put your last name: ")
country = input("put your country: ")
age = input("put your age: ")