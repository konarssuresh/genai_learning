def calculate_bill(cups=0, price_per_cup=0):
    return round(cups*price_per_cup,2)


print(calculate_bill(10,3))