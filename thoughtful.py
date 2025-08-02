'''
EXPLORE:
Write a Python function sort(width, height, length, mass) that:
   - Calculates the volume = w * h * l 
   - Checks 3 conditions: 
    Bulky: volume >= 1 million or any dimension >= 150 
    Heavy: mass (is density times volume) >= 20 
   - Then dispatch the result to one of these categories:
      - "REJECTED" - both bulky and heavy 
      - "SPECIAL" - either bulky or heavy (not both)
      - "STANDARD" - neither 


      
'''

def sort(width, height, length, mass):
    # stores the formula for volume in its correct variable 
    volume = width * height * length
    # determines if the package is bulky by volume or dimensions
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150

    # stores true or false if the mass is greater than 20
    is_heavy = mass >= 20

    # if is_heavy and is_bulky:
    #     return "REJECTED"
    # elif is_bulky:
    #     return "SPECIAL"
    # elif is_heavy:
    #     return "SPECIAL"
    # else:
    #     return "STANDARD"

    return "REJECTED" if is_heavy and is_bulky else "SPECIAL" if is_bulky or is_heavy else "STANDARD" 


# print(sort(100, 100, 100, 10))  # Expected: "SPECIAL"
# print(sort(10, 10, 10, 5))  # 1000 cm³, 5 kg → Expected: "STANDARD"
# print(sort(10, 10, 10, 25))  # 1000 cm³, 25 kg → Expected: "SPECIAL"
# print(sort(200, 200, 200, 30))  # Massive volume and 30 kg → Expected: "REJECTED"

# ✅ Sample test cases
if __name__ == "__main__":
    print(sort(10, 10, 10, 5))       # STANDARD
    print(sort(100, 100, 100, 10))   # SPECIAL (bulky)
    print(sort(10, 10, 10, 25))      # SPECIAL (heavy)
    print(sort(200, 200, 200, 30))   # REJECTED



    
