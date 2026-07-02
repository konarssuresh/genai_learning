# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams

print(f"total grams of base tea {total_grams}")

remaining_tea = black_tea_grams - ginger_grams

print(f"total grams of remaining tea {remaining_tea}")

milk_litres = 7
serving =4
milk_per_serving = milk_litres/serving

print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots =4
bags_per_pots = total_tea_bags // pots

print(f"whole tea bags per pot {bags_per_pots}")

total_cardemom_pots = 10
pods_per_cup = 3
leftover_pods = total_cardemom_pots % pods_per_cup
print(f"leftover c pods {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"powerfuul flavour scaled - {powerful_flavour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(total_tea_leaves_harvested)
