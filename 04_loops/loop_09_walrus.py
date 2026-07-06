# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ['small','medium','large']

# if (requested_size := input("enter your cup size:  ")) in available_sizes:
#     print(f"this size is available - serving {requested_size} chai")
# else:
#     print(f"{requested_size} is not available")



flavours = ['masala','ginger','lemon','mint']

print(f"available flavours - {flavours}")

while(flavor := input("choose yor flavour: -")) not in flavours:
    print(f"Sorry {flavor} is not available")

print(f"You chose {flavor} chai")