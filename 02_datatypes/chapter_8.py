#  mutable - List/Array

ingredients = ['water','milk','black tea']

ingredients.append('sugar')

print(f"ingredients : {ingredients}")

ingredients.remove('water')

print(f"ingredients after removing : {ingredients}")

spice_options = ['ginger','cardemom']
chai_ingredients = ['water','milk']

chai_ingredients.extend(spice_options)

print(chai_ingredients)

chai_ingredients.insert(2,'black tea')
print(chai_ingredients)


last_added = chai_ingredients.pop()
print(f"last added -{last_added}")
chai_ingredients.reverse()
print(f"list - {chai_ingredients}")


chai_ingredients.sort()
print(f"sorted list {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level {max(sugar_levels)}")
print(f"Minimum sugar level {min(sugar_levels)}")

# operator overloading 

base_liquid = ['water','milk']
extra_flavour = ['ginger']

full_liq_mix = base_liquid  + extra_flavour

print(f"full list {full_liq_mix}")

strong_brew = ['black tea','water'] * 3

print(f"strong brew =. {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
print(f"raw byte data {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARDEMOM")
print(f"raw byte data {raw_spice_data}")



