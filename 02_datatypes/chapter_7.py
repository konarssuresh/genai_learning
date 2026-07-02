# tuples 
masala_spices = ("cardemom","clove","cinnamon")

(spice1,spice2,spice3) = masala_spices

print(f"main masala spices {spice1},{spice2},{spice3}")

ginger_ratio,cardemom_ratio = 2,1

print(f"Ratios is c {cardemom_ratio} and g {ginger_ratio}")

ginger_ratio, cardemom_ratio = cardemom_ratio, ginger_ratio

# membership

print(f"is ginger in masala spices? {'ginger' in masala_spices}")
print(f"is cinnamon in masala spices? {'cinnamon' in masala_spices}")