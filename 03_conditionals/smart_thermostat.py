device_status ="active"
temp = 38

if device_status  =="active":
    if temp > 35:
        print("high temp alert")
    else:
        print("temp is normal")
else:
    print("device is offline")