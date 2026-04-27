staff = [("Amit",16), ("Sarah",21), ("Ravi",15)]

for name, age in staff:
    if age <=18:
        print(f"{name}is eligible to manage staff")
        break
    
else:
    print(f"No one is eligible to manage staff")
