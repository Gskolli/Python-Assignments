# WAP to find your AGE

birth_year = int(input("enter the birth year: \t"))
print('age of person :', 2023 - birth_year)

# WAP to build Tip Calculator (total amount + tip amount / total members)

ttl_amt = int(input("enter total amount: \t"))
tip_amt = int(input("enter tip amount: \t"))
ttl_members = int(input("enter total members: \t"))

result1 = int((ttl_amt + tip_amt)/ttl_members)

print("total amt with tip per person:",result1)

# WAP to build a BMI calculator using python

weight = float(input("enter the weight value in kg's:\t"))
height = float(input("enter the height value in ft:\t"))

Body_mass_index = (float(weight/height)* 0.3048)
print("BMI: ",Body_mass_index)