even_nos = [i for i in range(20) if i%2==0]
print(even_nos)


menu = [
    "Masala",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

iced_tea = [tea for tea in menu if "iced" in tea.lower()]

print(iced_tea)

