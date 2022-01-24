"""Booleans operators."""

is_rainy: bool = True
is_cold: bool = False

print(not is_rainy)
print(not is_cold)
print(not True)
print(is_rainy and is_cold)
print(is_rainy or is_cold)

if is_rainy and is_cold: 
    print("bring a jacket")
else: 
    print("dont")

if is_rainy or is_cold: 
    print("bring a jacket")
else: 
    print("dont")
