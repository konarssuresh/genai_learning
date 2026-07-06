flavour = ['ginger','out of stock','lemon','discontinued','tulsi']

for current_flavour in flavour:
    if current_flavour == 'out of stock':
        continue
    if current_flavour == 'discontinued':
        break
    print(f"current flavor is {current_flavour}, it is available and marked done")