flavours = ["Ginger","Tulsi","Out of Stock","Lemon","Discontinued","Coffee"]

for flavour in flavours:
    if flavour=="Out of Stock":
        continue
    if flavour=="Discontinued":
        break
    print(f"{flavour} item found")

print(f"Outside of Loop")
