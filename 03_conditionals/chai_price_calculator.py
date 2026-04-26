cup =input("choose your cup size(small/medium/larger):").lower()

if cup == 'small':
    print("10Rs")
elif cup == "medium":
    print("15Rs")
elif cup =="large":
    print("20Rs")
else:
    print("unknown cup size")