seat_type = input("enter seat type:   ")

seat_types = ("sleeper","AC",'general','luxury')

if seat_type in seat_types:
    if seat_type == 'sleeper':
        print("you can sleep in it/. No AC no sheets. new general is what i would say this is")
    elif seat_type == 'AC':
        print('seating and sleeping arrangement just like sleeper you get centralized ac, a sheet and pillow')
    elif seat_type == 'general':
        print("this is something which i only recommend when you have no money for ticket")
    elif seat_type == 'luxury':
        print("best experience for premium")
else:
    print("invalid seat type")