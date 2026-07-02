#  sets

essential_spices = {'cardemomm','ginger','cinnamon'}
optional_spices = {'cloves','ginger','blackk pepper'}

all_spices = essential_spices | optional_spices

print(f"all spices - {all_spices}")

common_spices = essential_spices & optional_spices

print(f"common spices - {common_spices}")


only_in_essential = essential_spices - optional_spices

print(f"only in essential - {only_in_essential}")

#  membership test 

print(f" is ginger in  optional spices - {'ginger' in optional_spices}")
