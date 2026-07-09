chai_menu = {'masala':30,'ginger':40}

try:
    chai_menu['elaichi']
except KeyError:
    print("Key you are trying to access does not exist")

print("Hello chaiCode")