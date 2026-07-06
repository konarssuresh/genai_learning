
def print_order(name,chai_type):
    print(f"Customer {name} ordered {chai_type} chai!")


orders = [("Hitesh","lemon"),("Jon","Green"),("Sam","Ginger"),("Arya","mint")]

for name_of_cus, type_of_tea in orders:
    print_order(name_of_cus,type_of_tea)