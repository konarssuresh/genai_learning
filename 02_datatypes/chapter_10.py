#  dictionaries

chai_order = dict(type="Masala Chai",size="large",sugar=2)
print(f"chai order - {chai_order}")

chai_recipe = {}
chai_recipe["base"]="black tea"
chai_recipe['liquid']='milk'


print(f"Recipe base: {chai_recipe['base']}")
print(f" is liquid in base recipe - {"liquid" in chai_recipe}")
print(f"Recipe : {chai_recipe}")
del chai_recipe['liquid']
print(f"Recipe : {chai_recipe}")

# member ship test 

print(f" is liquid in base recipe - {"liquid" in chai_recipe}")

# print(f"keys in order - {chai_order.keys()}")
# print(f"values in order {chai_order.values()}")
# print(f"items in order - {chai_order.items()}")

last_item = chai_order.popitem()
print(f"removed last item - {last_item}")

extra_spices = {'cardemom':"crushed","ginger":"sliced"}

chai_recipe.update(extra_spices)

print(f"updated repice - {chai_recipe}")

chai_size =chai_order.get("note","No Note")
print(f"customer Note - {chai_size}")