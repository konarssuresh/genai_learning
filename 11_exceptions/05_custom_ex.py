def brew_chai(flavor):
    arr = ['masala','ginger','elaichi']

    if flavor not in arr:
        raise ValueError("invalid flavor")
    
    print(f"Brewing {flavor} chai")

brew_chai("masala")
brew_chai("mint")