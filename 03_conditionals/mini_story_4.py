device_status = 'active'
temperature = 30

if device_status == 'active':
    if temperature > 35:
        print("high temperature alarm")
    else:
        print("its normal")
else:
    print("device is offline")

    