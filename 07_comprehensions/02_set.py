even_no = {i for i in range(20) if i % 2 == 0}
print(even_no)

favorite_chais = [
    "Masala Chai",'Green Tea',"Masala Chai","Lemon Tea","Green Tea","Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais}
print(unique_chai)

recipes = {
    "Masala Chai": ['ginger','cardemom','clove'],
    "Elaichi Chai": ['cardemom','milk'],
    "Spicy Chai": ['ginger','Black pepper','clove']
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)