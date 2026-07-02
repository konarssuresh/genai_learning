spice_mix = set()
print(f"initial spice mix id :{id(spice_mix)}")
print(spice_mix)
spice_mix.add("Ginger")
spice_mix.add("Cardemom")
print(f"initial spice mix id :{id(spice_mix)}")
print(spice_mix)

new_set = spice_mix

new_set.add("test")
print(f"id of new set id {id(new_set)}")
print(f"new set {new_set}")
print(f"old set {spice_mix}")
