# for else

staff = [("Amit",15),("Raj",12),("Zara",17)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible staff")
else:
    print(f"no one is eligiblle to manage the staff")