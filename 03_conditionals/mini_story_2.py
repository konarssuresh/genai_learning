user_input = input("what do you want.  ")
inventory = {'cookie','samosa'}

if user_input.lower() in inventory:
    print("Order confirmed")
else:
    print("item unavailable")