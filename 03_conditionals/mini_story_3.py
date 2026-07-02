cup_sizes = ('small','medium','large')
user_input = input("enter size of cup you want and press enter(small,medium,large)? -").lower()

if user_input in cup_sizes:
    if user_input == 'small':
        print("10 rupee")
    elif user_input == 'medium':
        print("15 rupee")
    elif user_input == 'large':
        print("20 rupees")
else:
    print("size not available")

